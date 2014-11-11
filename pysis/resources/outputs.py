#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource

__service__ = 'Outputs'

__categoryFunctions__ = {'refrigeration' : 'getRefrigerationData'}

class Outputs(Resource):
        
    def __str__(self):
        return '<Outputs>'
    
    def getData(self):
        
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        assert isinstance(self.id, int)
        
        service = self.importService(__service__)
        func = __categoryFunctions__[self.output_type['category']]
        
        return getattr(service, func)(self.id)
    
