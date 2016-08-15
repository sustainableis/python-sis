# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.utilities import Utilities

class GetMeters(Request):
	uri = 'utilities/meters/{id}'
	resource = Utilities

	def clean_uri(self):
        if self.building_id:
            return 'buildings/{id}/utilities/meters'
        elif self.id:
            return uri
		else:
			return 'utilities/meters'

class GetAccounts(Request):
	uri = 'utilities/accounts/{id}'
	resource = Utilities

	def clean_uri(self):
		if not self.id:
			return 'utilities/accounts'

class GetStatements(Request):
	uri = 'utilities/statements/{id}'
	resource = Utilities

	def clean_uri(self):
		if self.id:
            return uri
        elif self.meter_id:
            return 'utilities/meters/{meter_id}/statements'
        else
			return 'utilities/statements'

class GetStatementTree(Request):
    uri = 'utilities/statements/{id}/tree'
    resource = Utilities

    def clean_uri(self):
        if not self.id:
            return 'utilities/statements/{id}/tree'

class SetStatement(Request):
    uri = 'utilities/statements/{id}'
    resource = Utilities

    def clean_uri(self):
        if not self.id:
            return 'utilities/statements/{id}'

class SetMeter(Request):
    uri = 'utilities/meters/{id}'
    resource = Utilities

    def clean_uri(self):
        if not self.id:
            return 'utilities/meters/{id}'
# 
""" Examples below using _get, _post, _put, and _del

def createReport(self, data = None):

        request = self.request_builder('reports.createReport', body=data)

        return self._post(request)

    def getReport(self, id = None):
        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.getReport', id = id)

        return self._post(request)

    def getReportByFacID(self, rid = None, fid = None):
        try:
            u = UUID(rid);
        except ValueError:
            print('id must be a valid UUID')
            return
        #{{url}}/v1/facilities/65/reporting/reports/059a5db5-f507-492c-ab22-59ad20b8daa2
        request = self.request_builder('reports.getReportByFacID', rid = rid, fid = fid)

        return self._get(request)


    def updateReport(self, id = None, data = None):
        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.updateReport', id = id, body = data)

        return self._put(request)

    def removeReport(self, id = None):
        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.removeReport', id = id)

        return self._del(request)
"""