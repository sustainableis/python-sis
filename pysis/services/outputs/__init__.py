# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Outputs(Service):
    """ 
    Consume `Outputs API <http://api.sustainableis.com/v1/outputs>`_ 
    
    Example uses:
    ------------
    TODO
    s.organizations.create({'name': 'Sample Organization'})
    org = s.organizations.get(id=30)
    s.organizations.update(30, {'name': 'Org Name'})
    s.organizations.delete(30)
    """

    def __init__(self, client):
        super(Outputs, self).__init__(client)
    
    def get(self, id=None):
        """ Get a specific output or all of them if id=None
        
        :returns A :doc:`response`
        """
        if id is None:
            request = self.request_builder('outputs.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('outputs.get', id=id)
            
        return self._get(request)
    
    def getRefrigerationData(self, id=None):
        """ Get the refrigeration data of an output
        
        :returns A :doc:`response`
        """
        assert isinstance(id, int)
        request = self.request_builder('outputs.getRefrigerationData', id=id)
        return self._get(request)
        
        
        