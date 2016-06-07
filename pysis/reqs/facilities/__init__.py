# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.utilities import UtilitySummary
from pysis.resources.facilities import Facilities
from pysis.resources.facilities import FacilityInfo
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


class GetUtilitySummary(Request):

    uri='facilities/{id}/utilities/summary'
    resource = UtilitySummary

    def clean_uri(self):

        uri = 'facilities/{id}/utilities/summary'

        params = []

        if self.statement_month:
            params.append('statement_month={statement_month}')

        if self.statement_year:
            params.append('statement_year={statement_year}')

        if len(params) > 0:
            uri += '?'
            for p in params[:-1]:
                uri += p + '&'
            else:
                uri += params[-1]

        return uri
    
class GetInfo(Request):
    uri = 'facilities/{id}/info'
    resource = FacilityInfo

    def clean_uri(self):

        return 'facilities/{id}/info'

