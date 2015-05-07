# -*- encoding: utf-8 -*-

from .base import Resource

__service__ = 'Feeds'

class Feeds(Resource):
        
    def __str__(self):
        return '<Feeds>'
    
    '''
    def __getattr__(self, attr):
        """Handles all services from a resource that use the id as an argument.
        
        Imports the necessary service, executes the request, and returns the resources.
        
        Args:
            attr (str): method called.
            
        Returns:
            Resource object(s)
            
        Raises:
            AttributeError: invalid method/service called.
        """        
        service = self.importService(__service__)
        if hasattr(service, attr):
            def wrapper(*args, **kw):
                if not hasattr(self, 'id'): 
                    raise AttributeError(str(self.id), "Service must have id")
                return getattr(service, attr)(self.id)
            return wrapper
        else:
            raise AttributeError(attr)
            
    '''
    
    def getConfigurations(self, environment=None):
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        
        service = self.importService(__service__)
        
        return service.getConfigurations(self.id, environment)
        
    def getConfigurationValues(self, environment=None):
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        
        service = self.importService(__service__)
        
        return service.getConfigurationValues(self.id, environment)
    
