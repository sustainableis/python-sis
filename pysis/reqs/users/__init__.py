# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.users import Users

class Get(Request):
    uri = 'users/{id}'
    resource = Users
    
    def clean_uri(self):
        if not self.id:
            return 'users'
    