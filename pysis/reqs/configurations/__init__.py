# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.configurations import Configurations

class Get(Request):
    uri = 'configurations/{id}'
    resource = Configurations
    
    def clean_uri(self):
        if not self.id:
            return 'configurations'
        
class Create(Request):
    uri = 'configurations'
    resource = Configurations
    
    body_schema = {
        'schema' : ('environment', 'title', 'description'),
        'required' : ('environment', 'title')   
    }
    
class Delete(Request):
    uri = 'configurations/{id}'
    resource = Configurations

class Update(Request):   
    uri = 'configurations/{id}'
    resource = Configurations    
