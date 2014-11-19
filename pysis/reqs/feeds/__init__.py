# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.feeds import Feeds
from pysis.resources.outputs import Outputs

class Get(Request):
    uri = 'feeds/{id}'
    resource = Feeds
    
    def clean_uri(self):
        if not self.id:
            return 'feeds'    

class GetOutputs(Request):
    uri = 'feeds/{id}/outputs'
    resource = Outputs
