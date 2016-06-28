# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.metrics import Metrics

class Get(Request):
	uri = 'metrics/{id}'
	resource = Metrics

	def clean_uri(self):
		if not self.id:
			return 'metrics'

class Set(Request):
	uri = 'metrics/{id}'
	resource = Metrics

	def clean_uri(self):
		if not self.id:
			return 'metrics/{id}'

class CreateMetric(Request):
    uri = 'metrics'
    
    def clean_uri(self):
        uri = 'metrics'

class RemoveMetric(Request):
    uri = 'metrics/{id}'
    
    def clean_uri(self):
        uri = 'metrics/{id}'

