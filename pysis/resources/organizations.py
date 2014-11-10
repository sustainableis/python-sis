#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource

__service__ = 'Organizations'

class Organizations(Resource):
        
    def __str__(self):
        return '<Organizations>'
    
    def getFacilities(self, id=None):  
        
        if hasattr(self, 'id'):
            _id = self.id
        else:
            _id = id 
        assert isinstance(_id, int)
        
        service = self.importService(__service__)
        return service.getFacilities(_id)
    
    def getBuildings(self, id=None):

        if hasattr(self, 'id'):
            _id = self.id
        else:
            _id = id 
        assert isinstance(_id, int)
        
        service = self.importService(__service__)
        return service.getBuildings(_id)
    
    def getUsers(self, id=None):

        if hasattr(self, 'id'):
            _id = self.id
        else:
            _id = id 
        assert isinstance(_id, int)
        
        service = self.importService(__service__)
        return service.getUsers(_id)
    
    def getFeeds(self, id=None):

        if hasattr(self, 'id'):
            _id = self.id
        else:
            _id = id 
        assert isinstance(_id, int)
        
        service = self.importService(__service__)
        return service.getFeeds(_id)
    
    def getOutputs(self, id=None):

        if hasattr(self, 'id'):
            _id = self.id
        else:
            _id = id 
        assert isinstance(_id, int)
        
        service = self.importService(__service__)
        return service.getOutputs(_id)
    
    def getBlastcells(self, id=None):

        if hasattr(self, 'id'):
            _id = self.id
        else:
            _id = id 
        assert isinstance(_id, int)
        
        service = self.importService(__service__)
        return service.getBlastcells(_id)
