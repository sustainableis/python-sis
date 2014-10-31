# -*- encoding: utf-8 -*-
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
    
from reqs.base import Request

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

    def __init__(self, **kwargs):

        #TODO: Add check for base_url in kwargs
        self.config = {
            'api_domain' : '',
            'base_url' : '',
            'token' : '',
            'extra_headers' : {'accept' : '*/*'}
        }
        
        self.config.update(kwargs)

        #Save OAauth2 token
        assert self.config['token'] != ''
        self.auth_header = 'Bearer %s' % self.config['token']
        self.default_headers['authorization'] = self.auth_header
            
        #TODO: All for extra connection properties
        #if self.config.extra_headers is not None:
        #    self.default_headers = _default_headers.copy()
        #    self.default_headers.update(self.config.extra_headers)  
        
        # Enforce case restrictions on self.default_headers
        #tmp_dict = {}
        #for k,v in self.default_headers.items():
        #    tmp_dict[k.lower()] = v
        #self.default_headers = tmp_dict      

    def head(self, url, headers={}, **params):
        url += self.urlencode(params)
        return self.request('HEAD', url, None, headers)

    def get(self, request, headers={}, **params):
        request.uri = "%s%s" % (self.config['base_url'], request.uri)
        request.uri += self.urlencode(params)
        response =  self.request('GET', str(request), None, headers)
        assert response[0] == 200
        return response

    def post(self, request, body=None, headers={}, **params):
        request.uri = "%s%s" % (self.config['base_url'], request.uri)
        request.uri += self.urlencode(params)
        if not 'content-type' in headers:
            # We're doing a json.dumps of body, so let's set the content-type to json
            headers['content-type'] = 'application/json'
        response = self.request('POST', str(request), json.dumps(body), headers)
        assert response[0] == 201
        return response

    def put(self, url, body=None, headers={}, **params):
        url += self.urlencode(params)
        if not 'content-type' in headers:
            # We're doing a json.dumps of body, so let's set the content-type to json
            headers['content-type'] = 'application/json'
        return self.request('PUT', url, json.dumps(body), headers)

    def delete(self, request, headers={}, **params):
        request.uri = "%s%s" % (self.config['base_url'], request.uri)
        request.uri += self.urlencode(params)
        response = self.request('DELETE', str(request), None, headers)
        assert response[0] == 204
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