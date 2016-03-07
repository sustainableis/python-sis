from pysis.services.base import Service
from uuid import UUID

class Reports(Service):
    """Reports Service

    Consumes Reports API: <{url}/reports>
    """
    def __init__(self, client):
        """Creates Reports object with a client"""
        super(Reports, self).__init__(client)

    def getAllReportTypes(self):

        request = self.request_builder('reports.getAllReportTypes')
        return self._get(request)

    def createReportType(self, data):

        request = self.request_builder('reports.types', body=data)

        return self._post(request)

    def getReportType(self, id=None):

        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return

        request = self.request_builder('reports.getReportType', id=id)

        return self._get(request)

    def updateReportType(self, id=None, data = None):

        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.updateReportType', id=id, body=data)

        return self._put(request)

    def removeReportType(self, id=None):
        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.removeReportType', id=id)

        return self._del(request)

    def getAllReports(self):

        request = self.request_builder('reports.getAllReports')

        return self._post(request)

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

    def getAllFacilityReports(self, id = None):
        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.getAllFacilityReports', id = id)

        return self._get(request)

    def createFacilityReport(self, fid = None, rid = None):
        try:
            u = UUID(rid);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.createFacilityReport', fid = fid, rid = rid)

        return self._post(request)

    def removeFacilityReport(self, id = None):
        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.removeFacilityReport', id=id)

        return self._del(request)

    def getReportSubscriptions(self, id = None):
        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.getReportSubscriptions', rid=id)

        return self._get(request)

    def addSubscriptionToReport(self, rid = None, sid = None):
        try:
            u = UUID(rid);
            u = UUID(sid);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.addSubscriptionToReport', rid = rid, sid = sid)

        return self._post(request)

    def removeSubscriptionFromReport(self, rid = None, sid = None):
        try:
            u = UUID(rid);
            u = UUID(sid);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.removeSubscriptionFromReport', rid = rid, sid = sid)

        return self._del(request)

    def getAllGeneratedReports(self, rid = None):
        try:
            u = UUID(rid);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.getAllGeneratedReports', rid = rid)

        return self._get(request)

    def createGeneratedReport(self, rid = None, data = None):
        try:
            u = UUID(rid);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.createGeneratedReport', rid = rid, body=data)

        return self._post(request)

    def addAttachmentToGenerateReport(self, gid = None, data = None):
        try:
            u = UUID(gid);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.addAttachmentToGenerateReport', gid = gid, body = data)

        return self._post(request)

    '''
    #below are prototype functions shamelessly stolen from the emails services for copy...  I mean inspiration
    def getSubscriptions(self, id=None, type=None):
        """Gets Email Subscriptions from the API

        Args:
            id (string): id of the email subscription.
                if None, returns all email_subscriptions
            type (string): type of the email_subscription


        Returns: email subscription resources
        """
        if id is None:

            params = {}
            if type:
                params['type'] = type

            request = self.request_builder('reports.getSubscriptions', **params)

        else:

            # try-parse UUID
            try:
                u = UUID(id);
            except ValueError:

                print('id must be a valid UUID')

                return

            request = self.request_builder('reports.getSubscriptions', id=id)

        return self._get(request)

    def createSubscription(self, subscription):

        request = self.request_builder('reports.createSubscription', body=subscription)

        return self._post(request)


    def triggerSubscription(self, id, data):

        # try-parse UUID
        try:
            u = UUID(id);
        except ValueError:

            print('id must be a valid UUID')

            return

        request = self.request_builder('reports.triggerSubscription', id=id, body=data)

        return self._post(request)
    '''
