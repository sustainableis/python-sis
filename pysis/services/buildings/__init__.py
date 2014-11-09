# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Buildings(Service):
    """ 
    Consume `Buildings API <http://api.sustainableis.com/v1/buildings>`_ 
    
    Example uses:
    ------------
    TODO
    s.organizations.create({'name': 'Sample Organization'})
    org = s.organizations.get(id=30)
    s.organizations.update(30, {'name': 'Org Name'})
    s.organizations.delete(30)
    """

    def __init__(self, client):
        super(Buildings, self).__init__(client)
    
    def get(self, id=None):
        """ Get a specific building or all of them if id=None
        
        :returns A :doc:`response`
        """
        if id is None:
            request = self.request_builder('buildings.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('buildings.get', id=id)
            
        return self._get(request)