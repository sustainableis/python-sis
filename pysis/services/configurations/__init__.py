# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Configurations(Service):
    """Configurations Service
    
    Consumes Configurations API: <{url}/configurations>    
    """

    def __init__(self, client):
        """Creates Configurations object with a client"""
        super(Configurations, self).__init__(client)
    
    def get(self, id=None):
        """Gets Configurations from the API
        
        Args:
            id (int): id of the configuration. 
                if None, returns all Configurations
        
        Returns: 
            Configurations resources        
        """
        if id is None:
            request = self.request_builder('configurations.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('configurations.get', id=id)
            
        return self._get(request)
    
    def create(self, data):
        """Create a Configuration
        
        Args:
            data (dict): {'environment': 'development', 'title' : 'pysis test', 'description' : 'desc' }
        
        Returns: 
            Response 
        """
        #TODO: Make sure name is not '' if the node server doesn't
        request = self.request_builder('configurations.create', body=data)
        return self._post(request)
    
    def delete(self, id):
        """Delete a Configuration
        
        Args:
            id (int): id of the configuration.  
            
        Returns: 
            Response  
        """
        assert isinstance(id, int)
        request = self.request_builder('configurations.delete', id=id)
        return self._delete(request)
    
    def update(self, id, data):
        """Update a Configuration
        
        Args:
            id (int): id of the configuration.
            data (dict): {'environment': 'development', 'title' : 'pysis test', 'description' : 'desc' }
            
        Returns: 
            Resource
        """
        assert isinstance(id, int)
        request = self.request_builder('configurations.update', id=id, body=data)
        return self._put(request)
        
    
    
        
        