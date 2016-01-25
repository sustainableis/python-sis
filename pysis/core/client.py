from __future__ import print_function
import json
import sys

if sys.version_info[0:2] > (3,0):
    import http.client
    import urllib.parse
else:
    import httplib as http
    http.client = http
    import urllib as urllib
    urllib.parse = urllib
    
from pysis.core.errors import SISError
from pysis.reqs.base import RequestBuilder

_default_headers = {
    #TODO: Header field names MUST be lowercase; this is not checked
    #TODO: what should user agent be?
    'user-agent': 'PySISUserAgent/v1'
    }
                
class Client(object):
    http_methods = (
            'head',
            'get',
            'post',
            'put',
            'delete',
            'patch',
            )

    default_headers = {}
    headers = None
    config = {
            'api_domain' : '',
            'base_url' : '',
            'access_token' : '',
            'refresh_token': '',
            'client_id': '',
            'client_secret': '',
            'extra_headers' : {'accept' : '*/*'}
        }

    refresh_enabled = False

    def __init__(self, **kwargs):

        #TODO: Add check for base_url
        self.config.update(kwargs)

        # load token data from file
        try:
            with open('token') as token_file:
                token_data_string = token_file.read()

                token_data = json.loads(token_data_string)
        except IOError:
            print('Unable to open token file!')
            sys.exit(1)
        except ValueError:
            print('Token file incorrectly formatted!')
            sys.exit(1)

        if 'access_token' not in token_data:
            raise Exception('acess_token must be provided in token file!')

        # check that we have everything we need
        if all (k in token_data for k in ("refresh_token", "client_id", "client_secret")):
            print('Automatic token refresh enabled')
            self.refresh_enabled = True

        self.config.update(token_data)

        self.auth_header = 'Bearer %s' % self.config['access_token']
        self.default_headers['authorization'] = self.auth_header

        self.request_builder = RequestBuilder()

        #TODO: All for extra connection properties
        #if self.config.extra_headers is not None:
        #    self.default_headers = _default_headers.copy()
        #    self.default_headers.update(self.config.extra_headers)  
        
        # Enforce case restrictions on self.default_headers
        #tmp_dict = {}
        #for k,v in self.default_headers.items():
        #    tmp_dict[k.lower()] = v
        #self.default_headers = tmp_dict

    def refresh_token(self):

        if self.refresh_enabled:

            # get refreshed token
            formData = {'grant_type' : 'refresh_token',
               'client_id' : self.config['client_id'],
               'client_secret' : self.config['client_secret`'],
               'refresh_token' : self.config['refresh_token']
               }

            request = self.request_builder('oauth.refreshToken', body=formData)
            headers = headers={'content-type' : 'application/x-www-form-urlencoded'}

            try:
                response = self.post(request=request, body=request.body.content, headers=headers)
            except Exception as e:
                print('Error refreshing token: ' + e.message)

                return False


            print('New acces_token: ' + response.access_token)
            print('New refresh token: ' + response.refresh_token)

            # update tokens
            self.config['access_token'] = response.access_token
            self.config['refresh_token'] = response.refresh_token

            # store token information
            with open('token', 'w') as token_file:

                token_file.write(json.dumps({
                    'access_token': self.config['access_token'],
                    'refresh_token': self.config['refresh_token'],
                    'client_id': self.config['client_id'],
                    'client_secret': self.config['client_secret']
                }))

            return True

        else:
            return False


    def head(self, url, headers={}, **params):
        url += self.urlencode(params)
        return self.request('HEAD', url, None, headers)

    def get(self, request, headers={}, **params):
        request.uri = "%s%s" % (self.config['base_url'], request.uri)
        request.uri += self.urlencode(params)
        response =  self.request('GET', str(request), None, headers)
        SISError(str(request), response).process()
        return response

    def post(self, request, body=None, headers={}, **params):
        base_url = self.config['base_url']
        if request.uri == 'oauth/token':
            base_url = base_url[:-3]
        
        request.uri = "%s%s" % (base_url, request.uri)
        request.uri += self.urlencode(params)
        if not 'content-type' in headers:
            # We're doing a json.dumps of body, so let's set the content-type to json
            # Requests such as oauth can override this in the args
            #headers['content-type'] = 'application/json'
            headers['content-type'] = 'application/x-www-form-urlencoded'
        if headers['content-type'] == 'application/x-www-form-urlencoded':
            reqBody = urllib.parse.urlencode(body)
        else:
            reqBody = json.dumps(body)

        response = self.request('POST', str(request), reqBody, headers)

        SISError(str(request), response).process()
        return response

    def put(self, request, body=None, headers={}, **params):
        request.uri = "%s%s" % (self.config['base_url'], request.uri)
        request.uri += self.urlencode(params)
        if not 'content-type' in headers:
            # We're doing a json.dumps of body, so let's set the content-type to json
            headers['content-type'] = 'application/json'

        response = self.request('PUT', str(request), json.dumps(body), headers)

        SISError(str(request), response).process()

        return response

    def delete(self, request, headers={}, **params):
        request.uri = "%s%s" % (self.config['base_url'], request.uri)
        request.uri += self.urlencode(params)
        response = self.request('DELETE', str(request), None, headers)
        SISError(str(request), response).process()

        return response

    def patch(self, url, body=None, headers={}, **params):
        """
        Do a http patch request on the given url with given body, headers and parameters
        Parameters is a dictionary that will will be urlencoded
        """
        url += self.urlencode(params)
        if not 'content-type' in headers:
            # We're doing a json.dumps of body, so let's set the content-type to json
            headers['content-type'] = 'application/json'
        return self.request(self.PATCH, url, json.dumps(body), headers)

    def request(self, method, url, body, headers):
        '''Low-level networking. All HTTP-method methods call this'''

        headers = self._fix_headers(headers)
        
        conn = self.get_connection()
        conn.request(method, url, body, headers)
        response = conn.getresponse()
        status = response.status
        content = Content(response)
        self.headers = response.getheaders()
        conn.close()
        
        return status, content.processBody()

    def _fix_headers(self, headers):
        # Convert header names to a uniform case
        tmp_dict = {}
        for k,v in headers.items():
            tmp_dict[k.lower()] = v
        headers = tmp_dict

        # Add default headers (if unspecified)
        for k,v in self.default_headers.items():
            if k not in headers:
                headers[k] = v
        return headers

    def urlencode(self, params):
        if not params:
            return ''
        return '?' + urllib.parse.urlencode(params)

    def get_connection(self):
        conn = http.client.HTTPConnection(self.config['api_domain'])
        return conn
    
class Content(object):
    '''
    Decode a response from the server, respecting the Content-Type field
    '''
    def __init__(self, response):
        self.response = response
        self.body = response.read()
        (self.mediatype, self.encoding) = self.get_ctype()

    def get_ctype(self):
        '''Split the content-type field into mediatype and charset'''
        ctype = self.response.getheader('Content-Type')

        start = 0
        end = 0
        try:
            end = ctype.index(';')
            mediatype = ctype[:end]
        except:
            mediatype = 'x-application/unknown'

        try:
            start = 8 + ctype.index('charset=', end)
            end = ctype.index(';', start)
            charset = ctype[start:end].rstrip()
        except:
            charset = 'ISO-8859-1' #TODO

        return (mediatype, charset)

    def decode_body(self):
        '''
        Decode (and replace) self.body via the charset encoding
        specified in the content-type header
        '''
        self.body = self.body.decode(self.encoding)


    def processBody(self):
        '''
        Retrieve the body of the response, encoding it into a usuable
        form based on the media-type (mime-type)
        '''
        handlerName = self.mangled_mtype()
        handler = getattr(self, handlerName, self.x_application_unknown)
        return handler()


    def mangled_mtype(self):
        '''
        Mangle the media type into a suitable function name
        '''
        return self.mediatype.replace('-','_').replace('/','_')


    ## media-type handlers

    def x_application_unknown(self):
        '''Handler for unknown media-types'''
        return self.body

    def application_json(self):
        '''Handler for application/json media-type'''
        self.decode_body()

        try:
            pybody = json.loads(self.body)
        except ValueError:
            pybody = self.body

        return pybody

    text_javascript = application_json