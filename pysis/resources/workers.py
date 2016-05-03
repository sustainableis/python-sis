# -*- encoding: utf-8 -*-

from .base import Resource

__all__ = ('Workers', )
__service__ = 'Workers'

class Workers(Resource):
        
    def __str__(self):
        return '<Workers>'
    
    '''
    def __getattr__(self, attr):
        """Handles all services from a resource that use the uuid as an argument.
        
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
                if not hasattr(self, 'uuid'): 
                    raise AttributeError(str(self.uuid), "Service must have uuid")
                return getattr(service, attr)(self.uuid)
            return wrapper
        else:
            raise AttributeError(attr)
    '''
    
    def getConfigurations(self, environment=None):
        if not hasattr(self, 'uuid'): 
            raise AttributeError(str(self.uuid), "Service must have uuid")
        
        service = self.importService(__service__)
        
        return service.getConfigurations(self.uuid, environment)
        
    def getConfigurationValues(self, environment=None):
        if not hasattr(self, 'uuid'): 
            raise AttributeError(str(self.uuid), "Service must have uuid")
        
        service = self.importService(__service__)
        
        return service.getConfigurationValues(self.uuid, environment)


    def updateConfigurationValue(self, configuration_id, value_id, value, value_type):

        service = self.importService(__service__)

        return service.updateConfigurationValue(configuration_id, value_id, value, value_type)

    def createConfigurationValue(self, configuration_id, key, value, value_type):

        service = self.importService(__service__)

        return service.createConfigruationValue(configuration_id, key, value, value_type)

    def deleteConfigurationValue(self, configuration_id, value_id):

        service = self.importService(__service__)

        service.deleteConfigurationValue(configuration_id, value_id)

