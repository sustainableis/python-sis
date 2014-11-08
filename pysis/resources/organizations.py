#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource
from pysis.core.client import Client
from pysis.core.compat import import_module
from pysis.exceptions import (RequestDoesNotExist, UriInvalid,
                                  ValidationError, InvalidBodySchema)

__all__ = ('Organizations', )

class Organizations(Resource):
        
    def __str__(self):
        return '<Organizations>'
    
    def getFacilities(self, id=None):  
        
        if hasattr(self, 'id'):
            _id = self.id
        else:
            _id = id 
        assert isinstance(_id, int)
        
        
        module = import_module('pysis.services.organizations')
        service_class = getattr(module, 'Organizations')
        service = service_class(Client())
        return service.getFacilities(_id)

