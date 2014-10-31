# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Organizations(Service):
    """ 
    Consume `Organizations API <http://api.sustainableis.com/v1/organizations>`_ 
    """

    def __init__(self, **config):
        super(Organizations, self).__init__(**config)
    
    def get(self, id=None):
        """ Get a specific organization or all of them if id=None
        
        :returns A :doc:`result`
        """
        if id is None:
            request = self.request_builder('organizations.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('organizations.get', id=id)
            
        return self._get(request)
    
    def create(self, data):
        """ Create an organization
        
        """
        #TODO: Make sure name is not '' if the node server doesn't
        request = self.request_builder('organizations.create', body=data)
        return self._post(request)
    
    def delete(self, id):
        """ Delete an organizaiton
        
        """
        request = self.request_builder('organizations.delete', id=id)
        return self._delete(request)
        
        
        