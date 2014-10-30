# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.organizations import Organizations

class Get(Request):
    uri = 'organizations/{id}'
    resource = Organizations
    
    def clean_uri(self):
        if not self.id:
            return 'organizations'

#TODO: implement these

#class List(Request):
#    uri = 'users/{user}/orgs'
#    resource = Org
#
#    def clean_uri(self):
#        if not self.user:
#            return 'user/orgs'
#
#class Update(Request):
#    uri = 'orgs/{org}'
#    resource = Org
#    body_schema = {
#        'schema': ('billing_email', 'company', 'email', 'location', 'name'),
#        'required': (),
#    }
