# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.facilities import Facilities

class Get(Request):
    uri = 'facilities/{id}'
    resource = Facilities
    
    def clean_uri(self):
        if not self.id:
            return 'facilities'
        
class Create(Request):
    uri = 'facilities'
    resource = Facilities
    
    #TODO: 
    body_schema = {
        'schema' : ('name'),
        'required' : ('name')   
    }
    
class Delete(Request):
    uri = 'facilities/{id}'
    resource = Facilities

class Update(Request):   
    uri = 'facilities/{id}'
    resource = Facilities
    
    
