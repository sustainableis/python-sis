import unittest
import os
import logging
from pysis.workertools.logging_utils import MockHandler

LOG_FILE = '/tmp/test.log'
SAVED_FILE = '/tmp/saved_handler'

FIRST_LINE = {"foo": "bar"}
SECOND_LINE = {"baz": "quux"}


class HandlerTest(unittest.TestCase):
    def delete_files(self):
        if os.path.isfile(LOG_FILE):
            os.remove(LOG_FILE)
        if os.path.isfile(SAVED_FILE):
            os.remove(SAVED_FILE)

    def setUp(self):
        handler = MockHandler(filename=LOG_FILE, saved_file_name=SAVED_FILE)
        logger = logging.getLogger("test")
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        logger.info(FIRST_LINE)
        logger.info(SECOND_LINE)
        # make sure the close method is called
        del logger
        del handler

    def tearDown(self):
        self.delete_files()

    def test_write_and_save(self):
        self.assertTrue(os.path.isfile(LOG_FILE))
        self.assertTrue(os.path.isfile(SAVED_FILE))
        import json
        saved_text = open(SAVED_FILE).read().strip()
        self.assertEqual('saved', saved_text)
        saved_info = open(LOG_FILE).readlines()

        self.assertEqual(2, len(saved_info))
        info = [FIRST_LINE, SECOND_LINE]
        for i, l in enumerate(info):
            self.assertEqual(json.loads(saved_info[i]), l)