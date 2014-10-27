# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Organizations(Service):
    """ 
    Consume `Organizations API <http://api.sustainableis.com/v1/organizations>`_ 
    """

    def __init__(self, **config):
        super(Organizations, self).__init__(**config)
        
    def getAll(self):
        """ Get all organizations
        
        :returns A :doc:`result`
        """
        
        request = self.request_builder('organizations.get')
        return self._get(request)