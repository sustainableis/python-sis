# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.outputs import Outputs
from pysis.resources.fields import Fields
from pysis.resources.refrigeration import Refrigeration

class Get(Request):
    uri = 'outputs/{id}?{filterName}={filterValue}'
    resource = Outputs
    
    def clean_uri(self):
        uri = 'outputs'
        
        if self.id:
            uri += '/{id}'
            
        if self.filterName and self.filterName is not None:
            uri += '?{filterName}={filterValue}'

        return uri
        
class GetFields(Request):
    uri = 'outputs/{id}/fields'
    resource = Fields
        
class GetRefrigerationData(Request):
    uri = 'outputs/{id}/refrigerationData'
    resource = Refrigeration
    