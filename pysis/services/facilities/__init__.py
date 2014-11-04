# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Facilities(Service):
    """ 
    Consume `Facilities API <http://api.sustainableis.com/v1/facilities>`_ 
    
    Example uses:
    ------------
    """

    def __init__(self, **config):
        super(Facilities, self).__init__(**config)
    
    def get(self, id=None):
        """ Get a specific facility or all of them if id=None
        
        :returns A :doc:`result`
        """
        if id is None:
            request = self.request_builder('facilities.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('facilities.get', id=id)
            
        return self._get(request)
    
    def create(self, data):
        """ Create a facility
        
        """
        #TODO: Make sure name is not '' if the node server doesn't
        request = self.request_builder('facilities.create', body=data)
        return self._post(request)
    
    def delete(self, id):
        """ Delete a facility
        
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.delete', id=id)
        return self._delete(request)
    
    def update(self, id, data):
        """ Update a facility
        
        """
        assert isinstance(id, int)
        request = self.request_builder('facilities.update', id=id, body=data)
        return self._put(request)
        
        
        