#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource

__service__ = 'Organizations'

class Organizations(Resource):
             
    def __str__(self):
        return '<Organizations>'
    
    def __getattr__(self, attr):
        
        service = self.importService(__service__)
        if hasattr(service, attr):
            def wrapper(*args, **kw):
                if not hasattr(self, 'id'): 
                    raise AttributeError(str(self.id), "Service must have id")
                return getattr(service, attr)(self.id)
            return wrapper
        else:
            raise AttributeError(attr)
    
    
