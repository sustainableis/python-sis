# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Buildings(Service):
    """Buildings Service
    
    Consumes Feeds API: <{url}/buildings>    
    """

    def __init__(self, client):
        """Creates Buildings object with a client"""
        super(Buildings, self).__init__(client)
    
    def get(self, id=None):
        """Gets Buildings from the API
        
        Args:
            id (int): id of the building. 
                if None, returns all Buildings
        
        Returns: 
            Buildings resources        
        """
        if id is None:
            request = self.request_builder('buildings.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('buildings.get', id=id)
            
        return self._get(request)
    
    def getOutputs(self, id):
        """Get the outputs of a building
        
        Args:
            id (int): id of the building.
            
        Returns: 
            Outputs resources     
        """
        assert isinstance(id, int)
        request = self.request_builder('buildings.getOutputs', id=id)
        return self._get(request)
    
    def getBlastcells(self, id):
        """Get the blastcells of a building
        
        Args:
            id (int): id of the building.    
            
        Returns: 
            Blastcells resources 
        """
        assert isinstance(id, int)
        request = self.request_builder('buildings.getBlastcells', id=id)
        return self._get(request)
    
    