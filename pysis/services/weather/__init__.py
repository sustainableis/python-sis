# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Weather(Service):
    """Weather Service
    
    Consumes Weather API: <{url}/weather>    
    """

    def __init__(self, client):
        """Creates Weather object with a client"""
        super(Weather, self).__init__(client)
    
    def getAccounts(self, id=None):
        """Gets Weather Accounts from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Weather Accounts
        
        Returns: Weather resources      
        """
        if id is None:
            request = self.request_builder('weather.getAccounts')
        else:
            assert isinstance(id, int)
            request = self.request_builder('weather.getAccounts', id=id)
            
        return self._get(request)
    
    def getLocations(self, id=None):
        """Gets Weather Locations
        
        Args:
            id (int): id of the weather location. 
                if None, returns all Weather Locations
        
        Returns: Weather resource(s)      
        """
        if id is None:
            request = self.request_builder('weather.getLocations')
        else:
            assert isinstance(id, int)
            request = self.request_builder('weather.getLocations', id=id)
            
        return self._get(request)
        
    def getTypes(self, _type=""):
        """Gets Weather Locations
        
        Args:
            _type (str): string of the type. 
                if None, returns all Weather Types
        
        Returns: Weather resource(s)      
        """
        assert isinstance(_type, str)
        if len(_type) == 0:
            request = self.request_builder('weather.getTypes')
        else:
            request = self.request_builder('weather.getTypes', _type=_type)
            
        return self._get(request)

    def getActualHighs(self, id, dateStart="", dateEnd=""):
        """Get the temperature highs for the given date range
        
        Args:
            id (int): id of the location.
            dateStart (str): start date of the data
            dateEnd (str): end date of the data
            
        Returns: 
            Resource(s)  
        """
        assert isinstance(id, int)
        assert isinstance(dateStart, str)
        assert isinstance(dateEnd, str)
        
        request = self.request_builder('weather.getActualHighs', 
                                       id=id,
                                       dateStart=dateStart, 
                                       dateEnd=dateEnd)
        return self._get(request)
    
    def getActualTemps(self, id, dateStart="", hourStart=None, dateEnd="", hourEnd=None):
        """Get the hourly actual temperatures
        
        Args:
            id (int): id of the location.
            dateStart (str): start date of the data
            hourStart (int): hour(0..23) of the start date
            dateEnd (str): end date of the data
            hourEnd (int): hour(0..23) of the end date
            
            
        Returns: 
            Resource(s)  
        """
        assert isinstance(id, int)
        assert isinstance(dateStart, str)
        assert isinstance(dateEnd, str)
        assert isinstance(hourStart, (int, type(None)))
        assert isinstance(hourEnd, (int, type(None)))
        
        request = self.request_builder('weather.getActualTemps', 
                                       id=id,
                                       dateStart=dateStart, 
                                       hourStart=hourStart,
                                       dateEnd=dateEnd,
                                       hourEnd=hourEnd)
        return self._get(request)
    
    def getForecastDaily(self, id):
        """Gets daily forecasts for a weather location
        
        Args:
            id (int): id of the weather location. 
        
        Returns: Weather resource(s)      
        """
        assert isinstance(id, int)
        request = self.request_builder('weather.getForecastDaily', id=id)
            
        return self._get(request)
    
    def getForecastHourly(self, id):
        """Gets hourly forecasts for a weather location
        
        Args:
            id (int): id of the weather location. 
        
        Returns: Weather resource(s)      
        """
        assert isinstance(id, int)
        request = self.request_builder('weather.getForecastHourly', id=id)
            
        return self._get(request)
    