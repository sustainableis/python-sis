# -*- encoding: utf-8 -*-

from .base import Resource

__service__ = 'Reports'

class Reports(Resource):
        
    def __str__(self):
        return '<Reports>'

    def __getattr__(self, attr):
        """Handles all services from a resource that use the id as an argument.

        Imports the necessary service, executes the request, and returns the resources.

        Args:
            attr (str): method called.

        Returns:
            Resource object(s)

        Raises:
            AttributeError: invalid method/service called.
        """
        service = self.importService(__service__)
        if hasattr(service, attr):
            def wrapper(*args, **kw):
                if not hasattr(self, 'id'):
                    raise AttributeError(str(self.id), "Report must have id")
                return getattr(service, attr)(self.id)
            return wrapper
        else:
            raise AttributeError(attr)
    
    def getAllReportTypes(self):
        
        service = self.importService(__service__)
        
        return service.getAllReportTypes()

    def getAllReportTypes(self):
        service = self.importService(__service__)
        return service.getAllReportTypes()
        
    def createReportType(self):
        service = self.importService(__service__)
        return service.createReportType()
        
    def getReportType(self):
        if not hasattr(self, 'uuid'): 
            raise AttributeError(str(self.uuid), "Service must have uuid")
        #print self.uuid
        service = self.importService(__service__)
        return service.getReportType(id = self.uuid)

    def getReportTypeOrgs(self):
        if not hasattr(self, 'uuid'): 
            raise AttributeError(str(self.uuid), "Service must have uuid")
        #print self.uuid
        service = self.importService(__service__)
        return service.getReportTypeOrgs(id = self.uuid)
        
    def updateReportType(self):
        service = self.importService(__service__)
        return service.updateReportType()
        
    def removeReportType(self):
        service = self.importService(__service__)
        return service.removeReportType()
        
    def getAllReports(self):
        service = self.importService(__service__)
        return service.getAllReports()
        
    def createReport(self):
        service = self.importService(__service__)
        return service.createReport()
        
    def getReport(self):
        if not hasattr(self, 'uuid'): 
            raise AttributeError(str(self.uuid), "Service must have uuid")
        print self.uuid
        service = self.importService(__service__)
        return service.getReport(id = self.uuid)
        
    def updateReport(self):
        service = self.importService(__service__)
        return service.updateReport()
        
    def removeReport(self):
        service = self.importService(__service__)
        return service.removeReport()
        
    def getAllFacilityReports(self):
        service = self.importService(__service__)
        return service.getAllFacilityReports()
        
    def createFacilityReport(self):
        service = self.importService(__service__)
        return service.createFacilityReport()
        
    def removeFacilityReport(self):
        service = self.importService(__service__)
        return service.removeFacilityReport()
        
    def getReportSubscriptions(self):
        service = self.importService(__service__)
        return service.getReportSubscriptions()
        
    def addSubscriptionToReport(self):
        service = self.importService(__service__)
        return service.addSubscriptionToReport()
        
    def removeSubscriptionFromReport(self):
        service = self.importService(__service__)
        return service.removeSubscriptionFromReport()
        
    def getAllGeneratedReports(self):
        service = self.importService(__service__)
        return service.getAllGeneratedReports()
        
    def createGeneratedReport(self):
        service = self.importService(__service__)
        return service.createGeneratedReport()
        
    def addAttachmentToGenerateReport(self):
        service = self.importService(__service__)
        return service.addAttachmentToGenerateReport()
    
    def triggerReportSubscription(self):
        service = self.importService(__service__)
        return service.triggerReportSubscription()
