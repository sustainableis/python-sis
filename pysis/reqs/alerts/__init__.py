
from pysis.reqs.base import Request
from pysis.resources.alerts import Alerts


class Get(Request):
    uri='alerts/{id}'
    resource = Alerts

    def clean_uri(self):
        uri = 'alerts'

        params = []
        if self.id:
            uri += '/{id}'
        else:

            params = []
            if self.facility_id:
                params.append('facility_id={facility_id}')
            if self.is_active:
                params.append('is_active={is_active}')
            if self.alert_type_id:
                params.append('alert_type_id={alert_type_id}')

        if len(params) > 0:
            uri += '?'
            for p in params[:-1]:
                uri += p + '&'
            else:
                uri += params[-1]

        return uri


class Trigger(Request):

    uri = 'alerts/{id}/trigger'
    resource = Alerts

    def clean_uri(self):
        return 'alerts/{id}/trigger'


class Create(Request):

    uri = 'alerts'

    def clean_uri(self):

        return 'alerts'





