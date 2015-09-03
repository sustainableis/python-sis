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
        

    def executeStatement(self, table_name, statement, selectColumn, table_type):

        # note that selectColumn must be convertible to integer!

        # get a cursor
        cursor = self.conn.cursor();

        # execute statement
        cursor.execute(statement)

        highestSelectColumn = -1;

        # comprehend list of column names
        columns = [column[0] for column in cursor.description]

        # iterate over rows
        for row in cursor:

            #print 'tran_log_id: ' + str(row[0])

            # need to create a dict out of row
            data = {}

            for col_name in columns:

                data[col_name] = row[columns.index(col_name)]

            # add row to rabbit producer.. rabbit messages
            # will be sent according to the maximum size 
            self.rabbit.addRow(self.wms_system_id, table_name, table_type, data)


            # also need to keept rack of highest select column
            # so we know where to start next time. 
            if (int(row[columns.index(selectColumn)]) > highestSelectColumn):

                highestSelectColumn = int(row[0])

        # make sure to send the remainder
        self.rabbit.flushAndSend(self.wms_system_id, table_name, table_type)

        # store greatest tran log id for next invocation
        if table_name in self.config:

            self.updateConfigurationValue(table_name, str(highestSelectColumn))
        else:
            self.createConfigurationValue('integer', table_name, str(highestSelectColumn))

            

    def updateConfigurationValue(self, key, value):

        self.worker.updateConfigurationValue(self.configuration_id, self.valueIDs[key], value)


    def createConfigurationValue(self, type, key, value):

        self.worker.createConfigurationValue(self.configuration_id, type, key, value)

        
        
