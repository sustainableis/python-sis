from pysis import SIS
import os
import json
import pdb

class APITokenException(Exception):
    pass

class BaseWorker(object):
    
    def __init__(self, workerID, environment):
        self.apiToken = self.getAPIToken()
        self.env = environment
        self.uuid = workerID
        self.api = SIS(token=self.apiToken)
        self.config = self.loadConfiguration()
    
    def getAPIToken(self):
        token = None
        token = os.environ.get('API_TOKEN')
        if token is None:
            raise APITokenException('API_TOKEN environment variable not provided!')
        return token    
    
    
    def loadConfiguration(self):
        worker = self.api.workers.get(uuid=self.uuid)
        print worker.label
        configValues = worker.getConfigurationValues(environment=self.env)
        config = {}
        for value in configValues:
            if value.type == "integer":
                config[value.key] = int(value.value)
            elif value.type == "json":
                config[value.key] = json.loads(value.value)
            else:
                config[value.key] = str(value.value)
        return config
        
        
        
