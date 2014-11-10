# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Feeds(Service):
    """ 
    Consume `Feeds API <http://api.sustainableis.com/v1/feeds>`_ 
    
    Example uses:
    ------------
    TODO
    s.organizations.create({'name': 'Sample Organization'})
    org = s.organizations.get(id=30)
    s.organizations.update(30, {'name': 'Org Name'})
    s.organizations.delete(30)
    """

    def __init__(self, client):
        super(Feeds, self).__init__(client)
    
    def get(self, id=None):
        """ Get a specific feed or all of them if id=None
        
        :returns A :doc:`response`
        """
        if id is None:
            request = self.request_builder('feeds.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('feeds.get', id=id)
            
        return self._get(request)