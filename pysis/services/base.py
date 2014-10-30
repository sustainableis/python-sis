# -*- encoding: utf-8 -*-

from pysis.core.client import Client, ConnectionProperties
from pysis.core.errors import NotFound
from pysis.core.result import base
from pysis.reqs.base import Factory


class Service(object):
    """
    You can configure each service with this keyword variables:

    :param str token: Token to OAuth
    :param str base_url: To support another api
    
    You can configure ``verbose`` logging like `requests library <http://docs.
    python-requests.org/en/v0.10.6/user/advanced/#verbose-logging>`_
    """

    def __init__(self, **config):
        props = ConnectionProperties(
                    api_url = 'api.sustainableis.com',
                    secure_http = False,
                    extra_headers = {
                        'accept' :    '*/*'
                        }
                    )
        self.config = {'base_url' : 'http://api.sustainableis.com/v1/'}
        self._client = Client(**config)
        self._client.setConnectionProperties(props)
        self.request_builder = Factory()
    
    def _request(self, verb, request, **kwargs):
        self._client.request(verb, request, **kwargs)

    def _get(self, request, **kwargs):
        
        request.uri = "%s%s" % (self.config['base_url'], request.uri)
        response = self._client.get(request, headers={'authorization' : 'Bearer 1a765a554a2359feb69c62b8b73576376c236fca'})
        return request.resource.loads(response[1])
    
    #TODO: Add other types of requests (PUT, POST, DELETE, PATCH, etc...)
