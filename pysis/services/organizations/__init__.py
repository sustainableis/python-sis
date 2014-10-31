# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Organizations(Service):
    """ 
    Consume `Organizations API <http://api.sustainableis.com/v1/organizations>`_ 
    
    Example uses:
    ------------
    s.organizations.create({'name': 'Sample Organization'})
    org = s.organizations.get(id=30)
    s.organizations.update(30, {'name': 'Org Name'})
    s.organizations.delete(30)
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
        assert isinstance(id, int)
        request = self.request_builder('organizations.delete', id=id)
        return self._delete(request)
    
    def update(self, id, data):
        """ Update an organization
        
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.update', id=id, body=data)
        return self._put(request)
        
        
        