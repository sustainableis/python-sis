# -*- encoding: utf-8 -*-

from .base import Resource

__all__ = ('Users', )

class Users(Resource):
        
    def __str__(self):
        return '<Users>'
    
