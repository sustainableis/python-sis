
from pysis.reqs.base import Request
from pysis.resources.alerts import Alert
from pysis.resources.alerts import AlertEmailSubscription
from pysis.resources.alerts import TriggeredAlert


class Get(Request):
    uri='alerts/{id}'
    resource = Alert

    def clean_uri(self):
        uri = 'alerts'

        params = []
        if self.id:
            uri += '/{id}'
        else:

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
    resource = Alert

    def clean_uri(self):
        return 'alerts/{id}/trigger'


class Create(Request):

    uri = 'alerts'
    resource = Alert


    def clean_uri(self):

        return 'alerts'


class GetEmailSubscriptions(Request):

    uri = 'alerts'
    resource = AlertEmailSubscription

    def clean_uri(self):

        uri='alerts'

        if self.id:
            uri += '/{id}/emails/subscriptions'

        else:
            uri += '/emails/subscriptions'

        return uri


class LinkEmailSubscription(Request):

    uri = 'alerts'
    resource = AlertEmailSubscription

    def clean_uri(self):

        return 'alerts/{id}/emails/subscriptions/{email_subscription_id}'


class GetTriggeredAlerts(Request):

    uri = 'alerts/{id}/triggered'

    resource = TriggeredAlert

    def clean_uri(self):

        uri = 'alerts/{id}/triggered'

        params = []

        if self.timeStart:
            params.append('timeStart={timeStart}')
        if self.timeEnd:
            params.append('timeEnd={timeEnd}')

        if len(params) > 0:
            uri += '?'
            for p in params[:-1]:
                uri += p + '&'
            else:
                uri += params[-1]

        return uri






