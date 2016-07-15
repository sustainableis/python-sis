# -*- encoding: utf-8 -*-

from .base import Resource

__service__ = 'Facilities'

class Facilities(Resource):

    def __str__(self):
        return str(self.__dict__)
    
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
    
    def getUtilityStatements(self, year=None, month=None):
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        assert isinstance(self.id, int)
        if year:
            assert isinstance(year, int)
        if month:
            assert isinstance(month, int)
            assert month > 0 and month <= 12
        
        service = self.importService(__service__)
        return service.getUtilityStatements(self.id, year, month)
    
class FacilityInfo(Resource):

    def __str__(self):
        return '<FacilityInfo>'

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
