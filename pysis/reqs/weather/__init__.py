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
    
class GetActualTemps(Request):
    uri = 'weather/locations/{id}/actualtemps'
    resource = Weather
    
    def clean_uri(self):
        uri = 'weather/locations/{id}/actualtemps'
        
        params = [((self.dateStart and len(self.dateStart) > 0), 'dateStart={dateStart}'),
                  ((self.dateEnd and len(self.dateEnd) > 0), 'dateEnd={dateEnd}'),
                  (self.hourStart is not None, 'hourStart={hourStart}'),
                  (self.hourEnd is not None, 'hourEnd={hourEnd}')]
        
        
        #determine the number of params to add
        count = 0
        for use, _ in params:
            if use: count += 1
            
        if count > 0:
            uri += '?'
        
        for use, text in params:
            if use:
                uri += text
                count -= 1
                if count > 0:
                    uri += '&'
                else:
                    break
                
        return uri

class GetForecastDaily(Request):
    uri = 'weather/locations/{id}/forecast/daily'
    resource = Weather
    
class GetForecastHourly(Request):
    uri = 'weather/locations/{id}/forecast/hourly'
    resource = Weather
          
