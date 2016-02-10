# -*- encoding: utf-8 -*-

from .base import Resource

__service__ = 'Reports'

class Reports(Resource):
        
    def __str__(self):
        return '<Reports>'
    
    def getAllReportTypes(self):
        '''
        if not hasattr(self, 'uuid'): 
            raise AttributeError(str(self.uuid), "Service must have uuid")
        '''
        
        service = self.importService(__service__)
        
        return service.getAllReportTypes()

