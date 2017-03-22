# -*- coding: utf-8 -*-
from pysis.core.compat import import_module
from pysis.exceptions import RequestDoesNotExist

class Resource(object):
    """Resource Base Class
    
    Any GET on a service will return resources.
    
    Attributes:
        _maps (dict): map of contents
        _collection_maps (dict): collections
        _enableParamChecks (bool): If True, fields arguments will be checked before used.
    """
    _maps = {}
    _collection_maps = {}
    _enableParamChecks = True

    def __init__(self, attrs):
        """Initializes a resource object
        
        Attributes:
            _attrs (dict): All fields of the resource
        """
        self._attrs = attrs
        self.__set_attrs()

    @classmethod
    def setParamCheck(self, enableParamChecks):
        """Sets the param check class variable.
        
        Args:
            enableParamChecks (bool): Determines whether or not to check field params
        """
        assert isinstance(enableParamChecks, bool)
        self._enableParamChecks = enableParamChecks
        
    @property
    def enableParamChecks(self):
        return self._enableParamChecks
        
    def __set_attrs(self):
        for attr in self._attrs:
            setattr(self, attr, self._attrs[attr])

    def __str__(self):
        return "<%s>" % self.__class__.__name__

    def __repr__(self):
        return self.__str__()
    
    def importService(self, service):
        """Import a service class
        
        Args:
            service (str): Service object to return.
            
        Returns:
            Instance of the requested service class.
            
        Raises:
            RequestDoesNotExist: The service import failed.
        """
        from pysis.core.client import Client

        try:
            moduleName = 'pysis.services.' + service.lower()
            module = import_module(moduleName)
            service_class = getattr(module, service)
            service = service_class(Client())
        except ImportError:
            raise RequestDoesNotExist("'%s' module does not exist" % moduleName)
        
        return service

    @classmethod
    def loads(self, resource_chunk):
        """Gets the resources
        
        Args:
            resource_chunk (Resource(s)): List of raw resources or a single one
            
        Returns:
            Resource objects. A list if more than one.        
        """
        if isinstance(resource_chunk, list):
            return [self.__load(raw_resource) for raw_resource in resource_chunk]
        else:
            return self.__load(resource_chunk)
    
    @classmethod
    def __load(self, raw_resource):
        """Creates an individual resource
        
        Args:
            raw_resource (Resource): Raw resource
        
        Returns:
            instance of Resource object of the correct child type
        """
        def self_resource(func):
            def wrapper(resource, raw_resource):
                if resource == 'self':
                    resource = self
                return func(resource, raw_resource)
            return wrapper

        @self_resource
        def parse_map(resource, raw_resource):
            if hasattr(raw_resource, 'items'):
                return resource.__load(raw_resource)

        @self_resource
        def parse_collection_map(resource, raw_resources):
            # Dict of resources (Ex: Gist file)
            if hasattr(raw_resources, 'items'):
                dict_map = {}
                for key, raw_resource in raw_resources.items():
                    dict_map[key] = resource.__load(raw_resource)
                return dict_map
            # list of resources
            elif hasattr(raw_resources, '__iter__'):
                return [resource.__load(raw_resource)
                        for raw_resource in raw_resources]
        
        #print(str(raw_resource))
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
    """Base Resource Class
    
    Used only for class attribute instantiation
    """
    
    def __str__(self):
        return 'Raw resource which should be always have an override to the appropriate resource'
