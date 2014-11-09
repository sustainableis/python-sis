#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource
from pysis.core.client import Client
from pysis.core.compat import import_module

__all__ = ('Users', )

class Users(Resource):
        
    def __str__(self):
        return '<Users>'
    
