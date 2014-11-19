# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Feeds(Service):
    """Feeds Service
    
    Consumes Feeds API: <{url}/feeds>    
    """

    def __init__(self, client):
        """Creates Feeds object with a client"""
        super(Feeds, self).__init__(client)
    
    def get(self, id=None):
        """Gets Feeds from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Feeds
        
        Returns: Feeds resources        
        """
        if id is None:
            request = self.request_builder('feeds.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('feeds.get', id=id)
            
        return self._get(request)
    
    def getOutputs(self, id):
        """Get the outputs of a feed
        
        Args:
            id (int): id of the feed. 
            
        Returns: 
            Outputs resources 
        """
        assert isinstance(id, int)
        request = self.request_builder('feeds.getOutputs', id=id)
        return self._get(request)
    
    