from pysis import SIS
import os
import json
import pdb

class APITokenException(Exception):
    pass

class BaseWorker(object):
    
    def __init__(self, workerID, environment):
        self.env = environment
        self.uuid = workerID
        self.api = SIS()
        self.configuration_id = None

        # load configuration
        self.config = self.loadConfiguration()
    
    def loadConfiguration(self):
        self.worker = self.api.workers.get(uuid=self.uuid)
        print (self.worker.label)
        configValues = self.worker.getConfigurationValues(environment=self.env)
        config = {}


        for value in configValues:

            configValue = {}

            # store type
            configValue['type'] = value.type

            # store value
            if value.type == "integer":
                configValue['value'] = int(value.value)
            elif value.type == "json":
                configValue['value'] = json.loads(value.value)
            else:
                configValue['value'] = str(value.value)

            # store id
            configValue['id'] = value.id

            # store config dict
            config[value.key] = configValue

            # save configuration_id
            # should be the same each time
            # dumb, but whatever
            self.configuration_id = value.configuration_id

        return config

    def updateConfigurationValue(self, key, value):


        # update local value
        configValue = self.config[key]

        configValue['value'] = value

        # send along type so update completes properly
        value_type = configValue['type']

        value_id = configValue['id']

        self.worker.updateConfigurationValue(self.configuration_id, value_id, value, value_type)


    def getConfigurationValue(self, key):

        return self.config[key]['value']


    def createConfigurationValue(self, key, value, value_type):

        res = self.worker.createConfigurationValue(self.configuration_id, key, value, value_type)

        # load local values
        configValue = {'value': value, 'id': res.id, 'type': value_type}

        self.config[key] = configValue

        
