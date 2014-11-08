# -*- encoding: utf-8 -*-

from pysis.core.client import Client
from pysis.core.errors import NotFound
from pysis.core.result import base
from pysis.reqs.base import Factory


class Service(object):
    """
    You can configure each service with this keyword variables:

    :param str token: Token to OAuth2
    :param str base_url: To support another api
    
    You can configure ``verbose`` logging like `requests library <http://docs.
    python-requests.org/en/v0.10.6/user/advanced/#verbose-logging>`_
    """

    def __init__(self, client):
        self._client = client
        self.request_builder = Factory()
    
    def _request(self, verb, request, **kwargs):
        self._client.request(verb, request, **kwargs)

    def _get(self, request, **kwargs):
        
        response = self._client.get(request)
        return request.resource.loads(response[1])
    
    def _post(self, request, **kwargs):
        
        response = self._client.post(request, request.body.content)
        return response
    
    def _delete(self, request, **kwargs):
        
        response = self._client.delete(request)
        return response
    
    def _put(self, request, **kwargs):
        
        response = self._client.put(request, request.body.content)
        return response
    
    #TODO: Add other types of requests (PUT, POST, DELETE, PATCH, etc...)
