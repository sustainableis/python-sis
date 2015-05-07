# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.feeds import Feeds
from pysis.resources.outputs import Outputs

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
