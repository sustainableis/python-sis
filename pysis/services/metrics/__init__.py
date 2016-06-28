# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Metrics(Service):
    """ Metrics Service"""

    def __init__(self, client):
        """Creates Metrics object with a client"""
        super(Metrics, self).__init__(client)
    
    def get(self, id=None):
        """Gets Metrics from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Metrics
        
        Returns: Metrics resources      
        """
        if id is None:
            request = self.request_builder('metrics.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('metrics.get', id=id)

        return self._get(request)

    def set(self, id = None, data = None):
        '''
            pass data as a JSON object
        '''
        if id is None:
            print("id must be valid")
            return
        else:
            assert isinstance(id, int)
            request = self.request_builder('metrics.set', id=id, body = data)

        return self._put(request)

    def createMetric(self, data = None):
        request = self.request_builder('metrics.createMetric', body=data)

        return self._post(request)

    def removeMetric(self, id = None):
        assert isinstance(id, int)
        request = self.request_builder('metrics.removeMetric', id = id)

        return self._delete(request)

    

       