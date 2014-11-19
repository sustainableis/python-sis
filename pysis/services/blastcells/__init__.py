# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Blastcells(Service):
    """Blastcells Service
    
    Consumes Blastcells API: <{url}/blastcells>    
    """

    def __init__(self, client):
        """Creates Blastcells object with a client"""
        super(Blastcells, self).__init__(client)
    
    def get(self, id=None):
        """Gets Blastcells from the API
        
        Args:
            id (int): id of the blastcell. 
                if None, returns all Blastcells
        
        Returns: 
            Blastcells resources        
        """
        if id is None:
            request = self.request_builder('blastcells.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('blastcells.get', id=id)
            
        return self._get(request) 
        
        