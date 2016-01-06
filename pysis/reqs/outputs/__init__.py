# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.outputs import Outputs
from pysis.resources.fields import Fields
from pysis.resources.data import Data
from pysis.resources.metrics import Metric

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
        
class GetData(Request):
    uri = 'outputs/{id}/data'
    resource = Data
    
    def clean_uri(self):
        uri ='outputs/{id}/'
        
        if self.field and self.field != '':
            uri += 'fields/{field}/'
        uri += 'data'
        
        params = []
        if self.timeStart and self.timeStart is not None:
            params.append('timeStart={timeStart}')
            
        if self.timeEnd and self.timeEnd is not None:
            params.append('timeEnd={timeEnd}')
            
        if self.window is not None:
            params.append('window={window}')        
        
        if len(params) > 0:
            uri += '?'
            for p in params[:-1]:
                uri += p + '&'
            else:
                uri += params[-1]
        
        return uri
    

class GetMetrics(Request):
    uri='outputs/{id}/fields/{field}/{metric_name}'
    resource = Metric

    def clean_uri(self):

        params = []

        uri='outputs/{id}/fields/{field}/{metric_name}'

        if self.timeStart:
            params.append('timeStart={timeStart}')

        if self.timeEnd:
            params.append('timeEnd={timeEnd}')

        if len(params) > 0:
            uri += '?'
            for p in params[:-1]:
                uri += p + '&'
            else:
                uri += params[-1]

        return uri


    
    