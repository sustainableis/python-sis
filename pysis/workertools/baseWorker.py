from pysis import SIS
import os
import json
import pdb
import logging
from logging import FileHandler
from logging.handlers import TimedRotatingFileHandler
from pysis.workertools.api import APIFileSaver
from logging_utils import S3MetricFileHandler

class APITokenException(Exception):
    pass


class BaseWorker(object):
    WORKER_LOG_FILE = '/tmp/worker.log'
    METRIC_LOG_FILE = '/tmp/metrics.log'

    def __init__(self, workerID, environment):
        self.env = environment
        self.uuid = workerID
        self.config = self.loadConfiguration()
        self.api = SIS()
        self.configuration_id = None
        self.fileSaver = APIFileSaver(apiDBConnection=None,
                                      accessKeyID=self.config['aws-access-key-id']['value'],
                                      secretAccessKey=self.config['aws-secret-access-key']['value'])
        self.logger = self.init_logger()
        self.metric_logger = self.init_metric_logger()

    def init_metric_logger(self):
        metric_logger = logging.getLogger('worker.metric.{}'.format(self.__class__.__name__))
        metric_logger.setLevel(logging.DEBUG)
        # overwrite each time as we store it in the DB when done
        metrics_disk_handler = FileHandler(BaseWorker.METRIC_LOG_FILE, mode='w')
        s3_handler = S3MetricFileHandler(self.config)
        metric_logger.addHandler(s3_handler)
        metric_logger.addHandler(metrics_disk_handler)
        return metric_logger

    def init_logger(self):
        logger = logging.getLogger('worker')
        logger.setLevel(logging.DEBUG)
        disk_handler = TimedRotatingFileHandler(BaseWorker.WORKER_LOG_FILE, when='d')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        disk_handler.setFormatter(formatter)
        logger.addHandler(disk_handler)
        return logger

    def loadConfiguration(self):
        self.worker = self.api.workers.get(uuid=self.uuid)
        print (self.worker.label)
        configValues = self.worker.getConfigurationValues(environment=self.env)
        config = {}
        for value in configValues:
            configValue = {'type': value.type}
            # store value
            mapping = {'integer': int, 'json': json.loads}
            configValue['value'] = mapping.get(value.type, default=str)(value.value)
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


if __name__ == '__main__':
    w = BaseWorker(workerID='ccce6095-1e9d-6acc-0656-bd5fafa4102e',
                   environment='production')
    print()