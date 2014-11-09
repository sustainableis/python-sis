# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.buildings import Buildings

class Get(Request):
    uri = 'buildings/{id}'
    resource = Buildings
    
    def clean_uri(self):
        if not self.id:
            return 'buildings'
    