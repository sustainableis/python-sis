from pysis.reqs.base import Request


class GetAllReportTypes(Request):
    uri = 'reporting/types'
    def clean_uri(self):
        uri = 'reporting/types'

class CreateReportType(Request):
    uri = 'reporting/types'
    def clean_uri(self):
        uri = 'reporting/types'

class GetReportType(Request):
    uri = 'reporting/types/{id}'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/types/{id}'

class UpdateReportType(Request):
    uri = 'reporting/types/{id}'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/types/{id}'

class RemoveReportType(Request):
    uri = 'reporting/types/{id}'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/types/{id}'

class GetAllReports(Request):
    uri = 'reporting/reports'
    def clean_uri(self):
        uri = 'reporting/reports'

class CreateReport(Request):
    uri = 'reporting/reports'
    def clean_uri(self):
        uri = 'reporting/reports'

class GetReport(Request):
    uri = 'reporting/reports/{id}'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/reports/{id}'

class UpdateReport(Request):
    uri = 'reporting/reports/{id}'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/reports/{id}'

class RemoveReport(Request):
    uri = 'reporting/reports/{id}'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/reports/{id}'

class GetAllFacilityReports(Request):
    uri = 'facilities/{id}/reporting/reports'
    def clean_uri(self):
        #@TODO
        uri = 'facilities/{id}/reporting/reports'

class CreateFacilityReport(Request):
    uri = 'facilities/{f_id}/reporting/reports/{rid}'
    def clean_uri(self):
        #@TODO
        uri = 'facilities/{f_id}/reporting/reports/{rid}'

class RemoveFacilityReport(Request):
    uri = 'facilities/{f_id}/reporting/reports/{rid}'
    def clean_uri(self):
        #@TODO
        uri = 'facilities/{f_id}/reporting/reports/{rid}'

class GetReportSubscriptions(Request):
    uri = 'reporting/reports/{rid}/emails/subscriptions'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/reports/{rid}/emails/subscriptions'

class AddSubscriptionToReport(Request):
    uri = 'reporting/reports/{rid}/emails/subscriptions/{sid}'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/reports/{rid}/emails/subscriptions/{sid}'

class RemoveSubscriptionFromReport(Request):
    uri = 'reporting/reports/{rid}/emails/subscriptions/{sid}'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/reports/{rid}/emails/subscriptions/{sid}'

class GetAllGeneratedReports(Request):
    uri = 'reporting/reports/{rid}/generated'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/reports/{rid}/generated'

class CreateGeneratedReport(Request):
    uri = 'reporting/reports/{rid}/generate'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/reports/{rid}/generate'

class AddAttachmentToGenerateReport(Request):
    uri = 'reporting/generated/{gid}/attach'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/generated/{gid}/attach'

