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
            request = self.request_builder('organizations.get', id=1)
            
        return self._get(request)
