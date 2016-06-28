# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.buildings import Buildings
from pysis.resources.outputs import Outputs
from pysis.resources.blastcells import Blastcells
from pysis.resources.metrics import Metrics

class Get(Request):
    uri = 'buildings/{id}'
    resource = Buildings
    
    def clean_uri(self):
        if not self.id:
            return 'buildings'
        
class GetOutputs(Request):
    uri = 'buildings/{id}/outputs'
    resource = Outputs

class GetBlastcells(Request):
    uri = 'buildings/{id}/blastcells'
    resource = Blastcells

class GetInfo(Request):
	uri = 'buildings/{id}/info'
	resource = Buildings
    
	def clean_uri(self):
		if not self.id:
			return 'buildings/{id}/info'

class GetMetricsScores(Request):
    uri = 'buildings/{id}/metrics/energystar'
    resource = Metrics
    
    def clean_uri(self):
        if not self.id:
            return 'buildings/{id}/metrics'

class GetMetrics(Request):
    uri = 'buildings/{id}/metrics'
    resource = Metrics
    
    def clean_uri(self):
        if not self.id:
            return 'buildings/{id}/metrics'

class Set(Request):
    uri = 'buildings/{id}'
    resource = Buildings
    
    def clean_uri(self):
        if not self.id:
            return 'buildings/{id}'
