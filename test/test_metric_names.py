import unittest
import inspect
import os
import logging
import json
from pysis.workertools.baseWorker import BaseWorker
from pysis.workertools.logging_utils import MockHandler

LOG_FILE = '/tmp/test.log'
SAVED_FILE = '/tmp/saved'

class BaseMockDatabaseWorker(BaseWorker):
    def __init__(self):
        self.metric_logger = self.init_metric_logger()

    def init_metric_logger(self):
        metric_logger = logging.getLogger('worker.metric.{}'.format(self.__class__.__name__))
        metric_logger.setLevel(logging.DEBUG)
        # overwrite each time as we store it in the DB when done
        metrics_disk_handler = MockHandler(filename=LOG_FILE, saved_file_name=SAVED_FILE, mode='w')
        metric_logger.addHandler(metrics_disk_handler)
        return metric_logger

    def onExit(self):
        pass

    def selectRowsByBlock(self):
        current_frame = inspect.currentframe()
        calling_frame = inspect.getouterframes(current_frame, 2)
        calling_frame_name = calling_frame[1][3]
        self.metric_logger.info({'foo': 'block', 'name': calling_frame_name})

    def selectRowsByRange(self):
        current_frame = inspect.currentframe()
        calling_frame = inspect.getouterframes(current_frame, 2)
        calling_frame_name = calling_frame[1][3]
        self.metric_logger.info({'foo': 'range', 'name': calling_frame_name})


class MockWorker(BaseMockDatabaseWorker):
    def getFoo(self):
        self.selectRowsByBlock()

    def getBar(self):
        self.selectRowsByRange()


class TestMethodName(unittest.TestCase):
    def delete_files(self):
        if os.path.isfile(LOG_FILE):
            os.remove(LOG_FILE)
        if os.path.isfile(SAVED_FILE):
            os.remove(SAVED_FILE)

    def setUp(self):
        worker = MockWorker()
        worker.getFoo()
        worker.getBar()
        del worker

    def tearDown(self):
        self.delete_files()

    def test_writes_log(self):
        self.assertTrue(os.path.isfile(LOG_FILE))
        data = open(LOG_FILE).readlines()
        data = [json.loads(d.strip()) for d in data]
        self.assertEqual(2, len(data))
        self.assertEqual({'foo': 'block', 'name': 'getFoo'}, data[0])
        self.assertEqual({'foo': 'range', 'name': 'getBar'}, data[1])

        self.assertTrue(os.path.isfile(SAVED_FILE))
        self.assertEqual('saved', open(SAVED_FILE).read().strip())