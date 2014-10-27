# -*- encoding: utf-8 -*-
import json
import base64
import sys
if sys.version_info[0:2] > (3,0):
    import http.client
    import urllib.parse
else:
    import httplib as http
    http.client = http
    import urllib as urllib
    urllib.parse = urllib

_default_headers = {
    #TODO: Header field names MUST be lowercase; this is not checked
    #TODO: what should user agent be?
    'user-agent': 'chetisawesome/v1'
    }

class ConnectionProperties(object):
    __slots__ = ['api_url', 'secure_http', 'extra_headers']

    def __init__(self, **props):#api_url = None, secure_http = None, extra_headers = None):
        # Initialize attribute slots
        for key in self.__slots__:
            setattr(self, key, None)
            
        #self.api_url = api_url
        #self.secure_http = secure_http
        #self.extra_headers = extra_headers

        # Fill attribute slots with custom values
        for key, val in props.items():
            if key not in ConnectionProperties.__slots__:
                raise TypeError("Invalid connection property: " + str(key))
            else:
                setattr(self, key, val)
                
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

    def __init__(self, username=None,
            password=None, token=None,
            connection_properties=None
            ):

        # Set up connection properties
        if connection_properties is not None:
            self.setConnectionProperties(connection_properties)

        # Set up authentication
        self.username = username
        if username is not None:
            if password is None and token is None:
                raise TypeError("You need a password to authenticate as " + username)
            if password is not None and token is not None:
                raise TypeError("You cannot use both password and oauth token authentication")

            self.auth_header = None
            if password is not None:
                self.auth_header = self.hash_pass(password)
            elif token is not None:
                self.auth_header = 'Bearer %s' % token #self.auth_header = 'Token %s' % token

    def setConnectionProperties(self, props):
        '''
        Initialize the connection properties. This must be called
        (either by passing connection_properties=... to __init__ or
        directly) before any request can be sent.
        '''
        if type(props) is not ConnectionProperties:
            raise TypeError("Client.setConnectionProperties: Expected ConnectionProperties object")

        self.prop = props
        if self.prop.extra_headers is not None:
            self.default_headers = _default_headers.copy()
            self.default_headers.update(self.prop.extra_headers)

        # Enforce case restrictions on self.default_headers
        tmp_dict = {}
        for k,v in self.default_headers.items():
            tmp_dict[k.lower()] = v
        self.default_headers = tmp_dict

    def head(self, url, headers={}, **params):
        url += self.urlencode(params)
        return self.request('HEAD', url, None, headers)

    def get(self, url, headers={}, **params):
        url += self.urlencode(params)
        response =  self.request('GET', url, None, headers)
        assert response[0] == 200
        return response

    def post(self, url, body=None, headers={}, **params):
        url += self.urlencode(params)
        if not 'content-type' in headers:
            # We're doing a json.dumps of body, so let's set the content-type to json
            headers['content-type'] = 'application/json'
        return self.request('POST', url, json.dumps(body), headers)

    def put(self, url, body=None, headers={}, **params):
        url += self.urlencode(params)
        if not 'content-type' in headers:
            # We're doing a json.dumps of body, so let's set the content-type to json
            headers['content-type'] = 'application/json'
        return self.request('PUT', url, json.dumps(body), headers)

    def delete(self, url, headers={}, **params):
        url += self.urlencode(params)
        return self.request('DELETE', url, None, headers)

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

        #if self.username:
        #headers['authorization'] = self.auth_header

        #TODO: Context manager
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

    def hash_pass(self, password):
        auth_str = ('%s:%s' % (self.username, password)).encode('utf-8')
        return 'Basic '.encode('utf-8') + base64.b64encode(auth_str).strip()

    def get_connection(self):
        if self.prop.secure_http:
            conn = http.client.HTTPSConnection(self.prop.api_url)
        elif self.username is None:
            conn = http.client.HTTPConnection(self.prop.api_url)
        else:
            conn = http.client.HTTPConnection(self.prop.api_url)
            #===================================================================
            # 
            # #TODO - ConnectionError
            # raise ValueError('Refusing to authenticate over'
            #         ' non-secure  (HTTP) connection. To override, edit'
            #         ' the source'
            #         )
            #===================================================================

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