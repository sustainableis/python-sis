# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.outputs import Outputs

class Get(Request):
    uri = 'outputs/{id}'
    resource = Outputs
    
    def clean_uri(self):
        if not self.id:
            return 'outputs'
    