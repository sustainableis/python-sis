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

        return self._post(request)

    def updateReportType(self, id=None, data = None):

        try:
            u = UUID(id);
        except ValueError:
            print('id must be a valid UUID')
            return
        request = self.request_builder('reports.updateReportType', id=id, body=data)

        return self._post(request)

    def removeReportType(self, subscription):

        request = self.request_builder('reports.removeReportType', body=subscription)

        return self._post(request)

    def getAllReports(self, subscription):

        request = self.request_builder('reports.getAllReports', body=subscription)

        return self._post(request)

    def createReport(self, subscription):

        request = self.request_builder('reports.createReport', body=subscription)

        return self._post(request)

    def getReport(self, subscription):

        request = self.request_builder('reports.getReport', body=subscription)

        return self._post(request)

    def updateReport(self, subscription):

        request = self.request_builder('reports.updateReport', body=subscription)

        return self._post(request)

    def removeReport(self, subscription):

        request = self.request_builder('reports.removeReport', body=subscription)

        return self._post(request)

    def getAllFacilityReports(self, subscription):

        request = self.request_builder('reports.getAllFacilityReports', body=subscription)

        return self._post(request)

    def createFacilityReport(self, subscription):

        request = self.request_builder('reports.createFacilityReport', body=subscription)

        return self._post(request)

    def removeFacilityReport(self, subscription):

        request = self.request_builder('reports.removeFacilityReport', body=subscription)

        return self._post(request)

    def getReportSubscriptions(self, subscription):

        request = self.request_builder('reports.getReportSubscriptions', body=subscription)

        return self._post(request)

    def addSubscriptionToReport(self, subscription):

        request = self.request_builder('reports.addSubscriptionToReport', body=subscription)

        return self._post(request)

    def removeSubscriptionFromReport(self, subscription):

        request = self.request_builder('reports.removeSubscriptionFromReport', body=subscription)

        return self._post(request)

    def getAllGeneratedReports(self, subscription):

        request = self.request_builder('reports.getAllGeneratedReports', body=subscription)

        return self._post(request)

    def createGeneratedReport(self, subscription):

        request = self.request_builder('reports.createGeneratedReport', body=subscription)

        return self._post(request)

    def addAttachmentToGenerateReport(self, subscription):

        request = self.request_builder('reports.addAttachmentToGenerateReport', body=subscription)

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
