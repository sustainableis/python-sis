# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Feeds(Service):
    """Feeds Service
    
    Consumes Feeds API: <{url}/feeds>    
    """

    def __init__(self, client):
        """Creates Feeds object with a client"""
        super(Feeds, self).__init__(client)
    
    def get(self, id=None, key=None):
        """Gets Feeds from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Feeds
            key (str): key of the feed
                can use this to search for a feed by key.Will be skipped if id is provided
        
        Returns: Feeds resources        
        """
        if id is None:
            if key is None:
                request = self.request_builder('feeds.get')
            else:
                request = self.request_builder('feeds.get', key=key)
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
    
    def getConfigurations(self, id, environment=None):
        """Get the configurations of a feed
        
        Args:
            id (int): id of the feed.  
            
        Returns: 
            Configurations resources   
        """
        assert isinstance(id, int)
        request = self.request_builder('feeds.getConfigurations', id=id, environment=environment)
        return self._get(request)
        
    def getConfigurationValues(self, id, environment=None):
        """Get the configuration values of a feed
        
        Args:
            id (int): id of the feed. 
            
        Returns: 
            Configurations resources   
        """
        assert isinstance(id, int)
        request = self.request_builder('feeds.getConfigurationValues', id=id, environment=environment)
        return self._get(request)


    def getTypes(self):

        request = self.request_builder('feeds.getTypes')
        return self._get(request)


    def update(self, id, updateData):

        request = self.request_builder('feeds.update', id=id, body=updateData)

        return self._put(request)
    