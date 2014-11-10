# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Blastcells(Service):
    """ 
    Consume `Blastcells API <http://api.sustainableis.com/v1/blastcells>`_ 
    
    Example uses:
    ------------
    s.organizations.create({'name': 'Sample Organization'})
    org = s.organizations.get(id=30)
    s.organizations.update(30, {'name': 'Org Name'})
    s.organizations.delete(30)
    """

    def __init__(self, client):
        super(Blastcells, self).__init__(client)
    
    def get(self, id=None):
        """ Get a specific blastcell or all of them if id=None
        
        :returns A :doc:`result`
        """
        if id is None:
            request = self.request_builder('blastcells.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('blastcells.get', id=id)
            
        return self._get(request) 
        
        