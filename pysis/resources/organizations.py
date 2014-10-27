#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource

__all__ = ('Organizations', )

class Organizations(Resource):

    def __str__(self):
        return '<Organizations>'
