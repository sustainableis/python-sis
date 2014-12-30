# -*- encoding: utf-8 -*-

from .base import Resource
from pysis.core.sis_datetime import convertToDateTime
from datetime import datetime

__service__ = 'Outputs'

class Outputs(Resource):
        
    def __str__(self):
        return '<Outputs>'
    
    def getFields(self):
        
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        assert isinstance(self.id, int)
                    
        service = self.importService(__service__)  
        return service.getFields(self.id)      
    
    def getData(self, timeStart=None, timeEnd=None, window=None, field=""):
        
        if not hasattr(self, 'id'): 
            raise AttributeError(str(self.id), "Service must have id")
        assert isinstance(self.id, int)
        assert isinstance(field, str)
        
        timeStart = convertToDateTime(timeStart)
        timeEnd = convertToDateTime(timeEnd)
        
        #Validate time parameters
        validTimeParams = [
                           (type(None), type(None), type(None)), #no time params
                           (datetime, datetime, int), #all time params
                           (datetime, type(None), int), #timeStart and window
                           (type(None), type(None), int) #window only
                           ] 
        timeElements = (type(timeStart), type(timeEnd), type(window))
        
        isTimeParamsValid = timeElements in validTimeParams        
        if not isTimeParamsValid:
            raise ValueError("Invalid combination of time parameters.")            
        
        service = self.importService(__service__)
        
        #Check the field name
        if self.enableParamChecks:
            outputFields = self.getFields()
            
            isValid = False
            for validField in outputFields:
                if field == validField.field_human_name:
                    isValid = True
                    break
            if not isValid: 
                raise ValueError("Invalid field name: '%s'" % field)
            
        return service.getData(self.id, timeStart, timeEnd, window, field)
    
    
    
