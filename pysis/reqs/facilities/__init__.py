# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.facilities import Facilities
from pysis.resources.buildings import Buildings
from pysis.resources.users import Users
from pysis.resources.feeds import Feeds
from pysis.resources.outputs import Outputs
from pysis.resources.blastcells import Blastcells

class Get(Request):
    uri = 'facilities/{id}'
    resource = Facilities
    
    def clean_uri(self):
        if not self.id:
            return 'facilities'
        
class GetBuildings(Request):
    uri = 'facilities/{id}/buildings'
    resource = Buildings
    
class GetUsers(Request):
    uri = 'facilities/{id}/users'
    resource = Users
    
class GetFeeds(Request):
    uri = 'facilities/{id}/feeds'
    resource = Feeds
    
class GetOutputs(Request):
    uri = 'facilities/{id}/outputs'
    resource = Outputs

class GetBlastcells(Request):
    uri = 'facilities/{id}/blastcells'
    resource = Blastcells
    
    
