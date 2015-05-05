# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.workers import Workers
from pysis.resources.configurations import Configurations

class Get(Request):
    uri = 'workers/{uuid}?{filterName}={filterValue}'
    resource = Workers
    
    def clean_uri(self):
        uri = 'workers'
        
        if self.uuid:
            uri += '/{uuid}'
            
        if self.filterName and self.filterValue is not None:
            uri += '?{filterName}={filterValue}'

        return uri

class GetConfigurations(Request):
    uri = 'workers/{uuid}/configurations'
    resource = Configurations
    
    def clean_uri(self):
        uri = 'workers/{uuid}/configurations'
        
        params = []
        if self.environment is not None:
            params.append('environment={environment}')
        
        if len(params) > 0:
            uri += '?'
            for p in params[:-1]:
                uri += p + '&'
            else:
                uri += params[-1]

        return uri