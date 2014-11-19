# -*- encoding: utf-8 -*-

from pysis.reqs.base import RequestBuilder


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
        response = self._client.get(request)
        return request.resource.loads(response[1])
    
    def _post(self, request, **kwargs):
        """POST request
        
        Args:
            request (Request): A valid request object
            kwargs (named dict): URL and header param variables
        
        Returns: 
            Resources        
        """
        response = self._client.post(request, request.body.content)
        return response
    
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
        response = self._client.put(request, request.body.content)
        return response


