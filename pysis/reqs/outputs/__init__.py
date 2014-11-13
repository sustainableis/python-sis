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
    
    def clean_uri(self):
        uri ='outputs/{id}/refrigerationData'
        
        if self.timeStart and self.timeStart is not None:
            uri += '?timeStart={timeStart}&timeEnd={timeEnd}&window={window}'
            
        if self.fields and len(self.fields) > 0:
            for i in range(len(self.fields)):
                uri += '&fields[]={fields[%s]}' % i
        
        return uri
    