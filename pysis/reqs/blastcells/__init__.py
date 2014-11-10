# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.blastcells import Blastcells

class Get(Request):
    uri = 'blastcells/{id}'
    resource = Blastcells
    
    def clean_uri(self):
        if not self.id:
            return 'blastcells'    
