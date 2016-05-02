from logging import Handler, FileHandler
import logging
import pika
from json import dumps


class QueueHandler(Handler):
    def __init__(self, config, file_saver):
        super(QueueHandler, self).__init__()
        credentials = pika.PlainCredentials(config['rabbit-user']['value'], config['rabbit-pass']['value'])
        params = pika.ConnectionParameters(host=config['rabbit-host']['value'], credentials=credentials)
        connection = pika.BlockingConnection(params)
        self.channel = connection.channel()
        self.rabbit_prefix = config['rabbit-prefix']['value']
        self.exchange_name = self.rabbit_prefix+'.wms_metrics'
        self.channel.exchange_declare(exchange=self.exchange_name, type='topic')

    def emit(self, record):
        try:
            self.channel.publish(exchange=self.exchange_name,
                                 routing_key='metrics',
                                 body=dumps(record))
        except:
            self.handleError(record)

    def flush(self):
        pass

    def close(self):
        try:
            self.channel.close()
        except Exception as e:
            logging.error('Unable to close publishing channel', e)


class MetricFileHandler(FileHandler):
    def close(self):
        super(MetricFileHandler, self).close()
        self.save_file()
    def save_file(self):
        pass


class S3MetricFileHandler(MetricFileHandler):
    def __init__(self, file_name, file_saver=None, mode='a', encoding=None, delay=0):
        super(S3MetricFileHandler, self).__init__(filename=file_name, mode=mode, encoding=encoding, delay=delay)
        self.file_saver = file_saver
        self.local_file_name = file_name
        # TODO -> need a meaningful name, maybe based on the docker container
        self.s3_file_name = ''

    def save_file(self):
        if self.file_saver is not None:
            self.file_saver.save_file(fileName=self.s3_file_name,
                                      file_category_id=None,
                                      local_filepath=self.local_file_name)