# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Workers(Service):
    """Workers Service
    
    Consumes Workers API: <{url}/workers>    
    """

    def __init__(self, client):
        """Creates Workers object with a client"""
        super(Workers, self).__init__(client)
    
    def get(self, uuid=None):
        """Gets Workers from the API
        
        Args:
            uuid (str): uuid of the worker. 
                if None, returns all Workers
        
        Returns: 
            Workers resources        
        """
        if uuid is None:
            request = self.request_builder('workers.get')
        else:
            assert isinstance(uuid, str)
            request = self.request_builder('workers.get', uuid=uuid)
            
        return self._get(request)
    
    def getConfigurations(self, uuid, environment=None):
        """Get the configurations of a worker
        
        Args:
            uuid (str): uuid of the worker.  
            
        Returns: 
            Configurations resources   
        """
        uuid = str(uuid)
        assert isinstance(uuid, str)
        request = self.request_builder('workers.getConfigurations', uuid=uuid, environment=environment)
        return self._get(request)

        
    def getConfigurationValues(self, uuid, environment=None):
        """Get the configurations of a worker
        
        Args:
            uuid (str): uuid of the worker.  
            
        Returns: 
            Configurations resources   
        """
        uuid = str(uuid)
        assert isinstance(uuid, str)
        request = self.request_builder('workers.getConfigurationValues', uuid=uuid, environment=environment)
        return self._get(request)

    def updateConfigurationValue(self, configuration_id, value_id, value):

        req_body = {'value': value}

        request = self.request_builder('workers.updateConfigurationValue', configuration_id=configuration_id, value_id=value_id, body=req_body)

        return self._put(request)

    def createConfigruationValue(self, configuration_id, type, key, value):

        req_body = {'type': type,
                    'key': key,
                    'value': value
                    }

        request = self.request_builder('workers.createConfigurationValue', configuration_id=configuration_id, body=req_body)

        return self._post(request)

