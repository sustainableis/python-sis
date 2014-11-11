#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource

__service__ = 'Outputs'

__categoryFunctions__ = {'refrigeration' : 'getRefrigerationData'}

__categoriesWithFields__ = ['refrigeration', 'sensor']

class Outputs(Resource):
        
    def __str__(self):
        return '<Outputs>'
    
    def getFields(self):
        
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        assert isinstance(self.id, int)
        
        if not self.output_type['category'] in __categoriesWithFields__:
            raise ValueError("This output category does not have fields")
            
        service = self.importService(__service__)  
        return service.getFields(self.id)      
    
    def getData(self):
        
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        assert isinstance(self.id, int)
        
        service = self.importService(__service__)
        func = __categoryFunctions__[self.output_type['category']]
        
        return getattr(service, func)(self.id)
    
    
    
