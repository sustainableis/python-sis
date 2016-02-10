from pysis.reqs.base import Request

class GetAllReportTypes(Request):
    uri='reporting/types'

    def clean_uri(self):
        uri = 'reporting/types'
