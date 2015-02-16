# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.weather import Weather

class GetAccounts(Request):
    uri = 'weather/accounts/{id}'
    resource = Weather
    
    def clean_uri(self):
        if not self.id:
            return 'weather/accounts' 
        
class GetLocations(Request):
    uri = 'weather/locations/{id}'
    resource = Weather
    
    def clean_uri(self):
        if not self.id:
            return 'weather/locations'
        
class GetTypes(Request):
    uri = 'weather/types/{_type}'
    resource = Weather
    
    def clean_uri(self):
        if not self._type:
            return 'weather/types' 
        
class GetActualHighs(Request):
    uri = 'weather/locations/{id}/actualhighs'   
    resource = Weather
    
    def clean_uri(self):
        uri = 'weather/locations/{id}/actualhighs'
        includeStart = self.dateStart and len(self.dateStart) > 0
        includeEnd = self.dateEnd and len(self.dateEnd) > 0
        
        if includeStart or includeEnd:
            uri += '?'
        
        if includeStart:
            uri += 'dateStart={dateStart}'
            if includeEnd:
                uri += '&'
            
        if includeEnd:
            uri += 'dateEnd={dateEnd}'
            
        return uri
    
          
