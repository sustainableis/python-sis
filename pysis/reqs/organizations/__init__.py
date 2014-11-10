# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.organizations import Organizations
from pysis.resources.facilities import Facilities
from pysis.resources.buildings import Buildings
from pysis.resources.users import Users
from pysis.resources.feeds import Feeds
from pysis.resources.outputs import Outputs
from pysis.resources.blastcells import Blastcells

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
    
class Delete(Request):
    uri = 'organizations/{id}'
    resource = Organizations

class Update(Request):   
    uri = 'organizations/{id}'
    resource = Organizations
    
class GetFacilities(Request):
    uri = 'organizations/{id}/facilities'
    resource = Facilities
    
class GetBuildings(Request):
    uri = 'organizations/{id}/buildings'
    resource = Buildings
    
class GetUsers(Request):
    uri = 'organizations/{id}/users'
    resource = Users
    
class GetFeeds(Request):
    uri = 'organizations/{id}/feeds'
    resource = Feeds
    
class GetOutputs(Request):
    uri = 'organizations/{id}/outputs'
    resource = Outputs

class GetBlastcells(Request):
    uri = 'organizations/{id}/blastcells'
    resource = Blastcells    

    
