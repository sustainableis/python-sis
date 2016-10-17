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

class GetReportTypeOrgs(Request):
    uri = 'reporting/types/{id}/organizations'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/types/{id}/organizations'

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

class GetReportByFacID(Request):
    uri = 'facilities/{fid}/reporting/reports/?report_type_id={rid}'
    #{{url}}/v1/facilities/65/reporting/reports/059a5db5-f507-492c-ab22-59ad20b8daa2
    def clean_uri(self):
        uri = 'facilities/{fid}/reporting/reports/?report_type_id={rid}'

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
    uri = 'facilities/{fid}/reporting/reports/{rid}'
    def clean_uri(self):
        #@TODO
        uri = 'facilities/{fid}/reporting/reports/{rid}'

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

class TriggerReportSubscription(Request):
    uri = 'reporting/generated/{gid}/trigger'
    def clean_uri(self):
        #@TODO
        uri = 'reporting/generated/{gid}/trigger'

