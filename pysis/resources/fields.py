# -*- encoding: utf-8 -*-

from .base import Resource

class Fields(Resource):
        
    def __str__(self):
        return str(self.__dict__)   
    
    
