# -*- encoding: utf-8 -*-

import json
from pysis.core.compat import import_module
from pysis.exceptions import (RequestDoesNotExist, ValidationError, InvalidBodySchema)
from pysis.resources.base import Raw
import traceback

ABS_IMPORT_PREFIX = 'pysis.reqs'

class Body(object):
    """Input's request handler 
    """

    def __init__(self, content, schema, required):
        """Body object. Used for inputs.
        
        Attributes:
            content (dict): Content of the request.
            schema (dict): Used to validate content.
            required (dict): Required fields for content.
        """
        self.content = content
        self.schema = schema
        self.required = required

    def dumps(self):
        """Dumps the content dictionary
        
        Returns:
            Content dictionary
        """
        if not self.schema:
            return self.content or None
        return json.dumps(self.parse())

    def parse(self):
        """Parse body with schema-required rules
        
        Returns:
            Parsed content dictionary
        
        Raises:
            ValidationError: A required content field is missing.
        """
        if not hasattr(self.content, 'items'):
            raise ValidationError("It needs a content dictionary (%s)" % (
                self.content, ))
        parsed = dict([(key, self.content[key]) for key in self.schema
                      if key in self.content])
        for attr_required in self.required:
            if attr_required not in parsed:
                raise ValidationError("'%s' attribute is required" %
                                      attr_required)
            if parsed[attr_required] is None:
                raise ValidationError("'%s' attribute can't be empty" %
                                      attr_required)
        return parsed


class Request(object):
    """Request class
    
    Contains the uri of the API and the content to send.
    
    Attributes:
        uri (str): URI of the API.
        resource (Resource): Raw resource object
        body_schema (dict): Schema of the Request headers
    """
    uri = ''
    resource = Raw
    body_schema = {}

    def __init__(self, **kwargs):
        """Body object. Used for inputs.
        
        Attributes:
            kwargs (dict): Args for the request, contains a key named 'body'.
        """
        self.body = kwargs.pop('body', {})
        self.args = kwargs
        self.clean()

    def __getattr__(self, name):
        return self.args.get(name)

    def __str__(self):
        return self.populate_uri()

    def populate_uri(self):
        """Populated the variables into the URI
        
        Returns:
            Populated URI ready to be sent to the server.
            
        Raises:
            ValidationError: variable in URI string is missing.
        """
        try:
            populated_uri = self.uri.format(**self.args)
        except KeyError:
            raise ValidationError(
                "'%s' request wasn't be able to populate the uri '%s' with "
                "'%s' args" % (self.__class__.__name__, self.uri, self.args))
        return str(populated_uri).strip('/')

    def clean(self):
        """Cleans the URI and body parameters
        """
        self.uri = self.clean_uri() or self.uri
        self.body = Body(self.clean_body(), **self._clean_valid_body())

    def clean_body(self):
        """Cleans the body parameters.
    
        Request child classes should override this method if cleaning is needed. 
        
        Returns:
            Body object
        """
        #TODO: Validate required schema
        return self.body

    def clean_uri(self):
        """Cleans the URI.
    
        Request child classes should override this method if cleaning is needed. 
        """
        return None

    def _clean_valid_body(self):
        """Validate the body is part of the schema
        
        Returns:
            Dictionary of schema and required body fields
            
        Raises:
            InvalidBodySchema: Body Schema is invalid 
        """
        schema = set(self.body_schema.get('schema', ()))
        required = set(self.body_schema.get('required', ()))
        if not required.issubset(schema):
            raise InvalidBodySchema(
                "'%s:valid_body' attribute is invalid. "
                "'%s required' isn't a subset of '%s schema'" % (
                self.__class__.__name__, required, schema))
        return dict(schema=schema, required=required)

    def get_body(self):
        """Gets the Body object as a dictionary
        
        Returns:
            Body (dict)
        """
        return self.body.dumps()


class RequestBuilder(object):
    """Request builder
    
    Breaks apart the URI and creates a Request
    """

    def __call__(self, request_uri, **kwargs):
        """Creates a request based off the class defined in the URI.
        
        Args:
            request_uri (str): URI of the request.
                String is split to get the needed request class
                
        Returns:
            Object of type Request (usually a child of Request)
            
        Raises:
            RequestDoesNotExist: Invalid request
        """
        module_chunk, _, request_chunk = request_uri.rpartition('.')
        request_chunk = request_chunk[0].upper() + request_chunk[1:]
        try:
            module = import_module('%s.%s' % (ABS_IMPORT_PREFIX, module_chunk))
            request_class = getattr(module, request_chunk)
            request = request_class(**kwargs)
            assert isinstance(request, Request)
            return request
        except ImportError:
            raise RequestDoesNotExist("'%s' module does not exist"
                                      % module_chunk)
        except AttributeError:

            raise RequestDoesNotExist("'%s' request does not exist in "
                                      "'%s' module" % (request_chunk,
                                      module_chunk))
            
