# -*- coding: utf-8 -*-

class Resource(object):

    _dates = ()
    _maps = {}
    _collection_maps = {}

    def __init__(self, attrs):
        self._attrs = attrs
        self.__set_attrs()

    def __set_attrs(self):
        for attr in self._attrs:
            setattr(self, attr, self._attrs[attr])

    def __str__(self):
        return "<%s>" % self.__class__.__name__

    def __repr__(self):
        return self.__str__()

    @classmethod
    def loads(self, resource_chunk):
        return [self.__load(raw_resource) for raw_resource in resource_chunk]
    
    @classmethod
    def __load(self, raw_resource):
        def self_resource(func):
            def wrapper(resource, raw_resource):
                if resource == 'self':
                    resource = self
                return func(resource, raw_resource)
            return wrapper
        
        new_resource = raw_resource.copy()
        new_resource.update(dict([
            (attr, parse_map(resource, raw_resource[attr]))
             for attr, resource in self._maps.items()
             if attr in raw_resource]))
        new_resource.update(dict([
            (attr, parse_collection_map(resource, raw_resource[attr]))
             for attr, resource in self._collection_maps.items()
             if attr in raw_resource]))

        return self(new_resource)

class Raw(Resource):

    def __str__(self):
        return 'Raw resource which should be alway have an override to the approriate resource'