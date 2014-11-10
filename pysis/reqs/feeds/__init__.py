# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.feeds import Feeds

class Get(Request):
    uri = 'feeds/{id}'
    resource = Feeds
    
    def clean_uri(self):
        if not self.id:
            return 'feeds'    
