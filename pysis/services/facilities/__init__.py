# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Facilities(Service):
    """Facilities Service
    
    Consumes Facilities API: <{url}/facilities>    
    """

    def __init__(self, client):
        """Creates Facilities object with a client"""
        super(Facilities, self).__init__(client)
    
    def get(self, id=None):
        """Gets Facilities from the API
        
        Args:
            id (int): id of the facility. 
                if None, returns all Facilities
        
        Returns: Facilities resources        
        """
        if id is None:
            request = self.request_builder('facilities.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('facilities.get', id=id)
            
        return self._get(request)
    
    def getBuildings(self, id):
        """Get the buildings of a facility
        
        Args:
            id (int): id of the facility. 
            
        Returns: 
            Buildings resources    
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.getBuildings', id=id)
        return self._get(request)
    
    def getUsers(self, id):
        """Get the users of a facility
        
        Args:
            id (int): id of the facility.    
            
        Returns: 
            Users resources 
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.getUsers', id=id)
        return self._get(request)
    
    def getFeeds(self, id):
        """Get the feeds of a facility
        
        Args:
            id (int): id of the facility. 
            
        Returns: 
            Feeds resources     
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.getFeeds', id=id)
        return self._get(request)
    
    def getOutputs(self, id):
        """Get the outputs of a facility
        
        Args:
            id (int): id of the facility.
            
        Returns: 
            Outputs resources    
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.getOutputs', id=id)
        return self._get(request)
    
    def getBlastcells(self, id):
        """Get the blastcells of a facility
        
        Args:
            id (int): id of the facility.  
            
        Returns: 
            Blastcells resources   
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.getBlastcells', id=id)
        return self._get(request)

    def getUtilitySummary(self, id, statement_month=None, statement_year=None):

        params = {}

        if statement_month:
            params['statement_month'] = statement_month

        if statement_year:
            params['statement_year'] = statement_year

        request = self.request_builder('facilities.getUtilitySummary', id=id, **params)

        return self._get(request)

    def getInfo(self, id):

        request = self.request_builder('facilities.getInfo', id=id)

        return self._get(request)
        

    def getBaseline(self, id):
        """Get the blastcells of a facility
        
        Args:
            id (int): id of the facility.  
            
        Returns: 
            Blastcells resources   
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.getBaseline', id=id)
        return self._get(request)
    
    
    def getUtilityMeters(self, id):
        """Get the utility meters of a facility
        
        Args:
            id (int): id of the facility.
            
        Returns: 
            Utility Meter resources    
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.getUtilityMeters', id=id)
        return self._get(request)
        
    def getUtilityStatements(self, id, year=None, month=None):
        
        params = {}

        if month:
            params['month'] = month

        if year:
            params['year'] = year

        request = self.request_builder('facilities.getUtilityStatements', id=id, **params)

        return self._get(request)
    
    def getOutputsTree(self, id, output_type=None):
        params = {}

        if output_type:
            params['output_type'] = output_type

        request = self.request_builder('facilities.getOutputsTree', id=id, **params)
        
        return self._get(request)
    
        
        
        