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

        # load configuration
        configs = self.loadConfiguration()
        self.config = configs['config']
        self.valueIDs = configs['valueIDs']
        self.configuration_id = configs['configuration_id']
    
    def getAPIToken(self):
        token = None
        token = os.environ.get('API_TOKEN')
        if token is None:
            raise APITokenException('API_TOKEN environment variable not provided!')
        return token    
    
    
    def loadConfiguration(self):
        self.worker = self.api.workers.get(uuid=self.uuid)
        print self.worker.label
        configValues = self.worker.getConfigurationValues(environment=self.env)
        config = {}
        valueIDs = {}
        configuration_id = None;


        for value in configValues:


            if value.type == "integer":
                config[value.key] = int(value.value)
            elif value.type == "json":
                config[value.key] = json.loads(value.value)
            else:
                config[value.key] = str(value.value)

            # save valueID
            valueIDs[value.key] = value.id

            # save configuration_id
            # should be the same each time
            configuration_id = value.configuration_id

        return {'config': config, 'valueIDs':valueIDs, 'configuration_id': configuration_id}
        



    def updateConfigurationValue(self, key, value):

        print 'Updatign config value for key:' + key + ', current id: '+ str(self.valueIDs[key])

        self.worker.updateConfigurationValue(self.configuration_id, self.valueIDs[key], value)


    def createConfigurationValue(self, type, key, value):

        self.worker.createConfigurationValue(self.configuration_id, type, key, value)

        
        
