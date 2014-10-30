# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.organizations import Organizations

class Get(Request):
    uri = 'organizations/{id}'
    resource = Organizations
    
    def clean_uri(self):
        if not self.id:
            return 'organizations'
class Create(Request):
    uri = 'organizations'
    resource = Organizations
    
    body_schema = {
        'schema' : ('name'),
        'required' : ('name')   
    }
