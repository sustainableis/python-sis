# -*- encoding: utf-8 -*-

from .base import Resource
from pysis.core.sis_datetime import convertToDateTime

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
    
    def getData(self, timeStart=None, timeEnd=None, window=None, fields=[]):
        
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        assert isinstance(self.id, int)
        assert isinstance(fields, list)
        
        timeStart = convertToDateTime(timeStart)
        timeEnd = convertToDateTime(timeEnd)
             
        requiredTimeElements = (timeStart, timeEnd, window)
        if requiredTimeElements.count(None) == len(requiredTimeElements) or \
            requiredTimeElements.count(None) == 0:
            pass
        else:
            raise ValueError("timeStart, timeEnd, and window should all be set if time is used")
        
        service = self.importService(__service__)
        
        if self.enableParamChecks and len(fields) > 0:
            outputFields = self.getFields()
            
            for f in fields:
                isValid = False
                for validField in outputFields:
                    if f == validField.field_human_name:
                        isValid = True
                        break
                if not isValid: 
                    raise ValueError("Invalid field name: '%s'" % f)
        
        func = __categoryFunctions__[self.output_type['category']]        
        return getattr(service, func)(self.id, timeStart, timeEnd, window, fields)
    
    
    
