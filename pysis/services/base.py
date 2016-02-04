# -*- encoding: utf-8 -*-
from __future__ import print_function
from pysis.reqs.base import RequestBuilder
from pysis.exceptions import InvalidAccessToken

def is_string(obj):
    try:
        obj + ''
        return True
    except TypeError:
        return False

class Service(object):
    """Service Base Class
    
    Handles all HTTP requests with the client
    """

    def __init__(self, client):
        """Creates a Service object with a client
        
        Attributes:
            request_builder (RequestBuilder): The request builder. 
        """
        self._client = client
        self.request_builder = RequestBuilder()

    def _get(self, request, **kwargs):
        """GET request
        
        Args:
            request (Request): A valid request object
            kwargs (named dict): URL and header param variables
        
        Returns: 
            Resources        
        """
        response = self._perform_request(lambda: self._client.get(request))

        return request.resource.loads(response[1])
    
    def _post(self, request, **kwargs):
        """POST request
        
        Args:
            request (Request): A valid request object
            kwargs (named dict): URL and header param variables
        
        Returns: 
            Resources        
        """
        
        if 'headers' not in kwargs:
            headers = {}
        else:
            headers = kwargs['headers']
        response = self._perform_request(lambda: self._client.post(request, body=request.body.content, headers=headers))
        if response[1] != None:
            if is_string(response[1]):
                return response[1]
            else:
                return request.resource.loads(response[1])
            
        return None
    
    def _delete(self, request, **kwargs):
        """DELETE request
        
        Args:
            request (Request): A valid request object
            kwargs (named dict): URL and header param variables
        
        Returns: 
            Resources        
        """
        response = self._client.delete(request)
        return response
    
    def _put(self, request, **kwargs):
        """PUT request
        
        Args:
            request (Request): A valid request object
            kwargs (named dict): URL and header param variables
        
        Returns: 
            Resources        
        """
        response = self._perform_request(lambda: self._client.put(request, request.body.content))

        return response


    def _perform_request(self, request_method):

        try:
            return request_method()

        except InvalidAccessToken as e:

            print('Access token invalid. Attempting refresh..')

            # call client's refresh token method
            if self._client.refresh_token():

                # now retry method
                return request_method()

            else:
                raise e





