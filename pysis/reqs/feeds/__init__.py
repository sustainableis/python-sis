# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.feeds import Feeds
from pysis.resources.outputs import Outputs
from pysis.resources.configurations import Configurations

class Get(Request):
    uri = 'feeds/{id}'
    resource = Feeds
    
    def clean_uri(self):
        uri = 'feeds'
        
        params = []
        if self.id:
            uri += '/{id}'
        elif self.key:
            params.append('key={key}')
        
        if len(params) > 0:
            uri += '?'
            for p in params[:-1]:
                uri += p + '&'
            else:
                uri += params[-1]
        
        return uri

class GetOutputs(Request):
    uri = 'feeds/{id}/outputs'
    resource = Outputs


class GetConfigurations(Request):
    uri = 'feeds/{id}/configurations'
    resource = Configurations
    
    def clean_uri(self):
        uri = 'feeds/{id}/configurations'
        
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

class GetConfigurationValues(Request):
    uri = 'feeds/{id}/configurations/values'
    resource = Configurations
    
    def clean_uri(self):
        uri = 'feeds/{id}/configurations/values'
        
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

class GetTypes(Request):
    uri = 'feeds/types'
    resource = Feeds

    def clean_uri(self):

        return 'feeds/types'


class Update(Request):
    uri='feeds/{id}'

    def clean_uri(self):
        uri = 'feeds'

        if self.id:
            uri += '/{id}'


