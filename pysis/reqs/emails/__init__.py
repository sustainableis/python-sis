from pysis.reqs.base import Request
from pysis.resources.emails import EmailSubscription, EmailSubscriptionTemplate

class GetSubscriptions(Request):
    uri='emails/subscriptions/{id]'
    resource = EmailSubscription

    def clean_uri(self):
        uri = 'emails/subscriptions'

        params = []

        if self.id:
            uri += '/{id}'

        else:
            if self.type:
                params.append('type={type}')

        if len(params) > 0:
            uri += '?'
            for p in params[:-1]:
                uri += p + '&'
            else:
                uri += params[-1]

        return uri

class TriggerSubscription(Request):

    uri = 'emails/subscriptions/{id}/trigger'
    resource = EmailSubscription

    def clean_uri(self):
        return 'emails/subscriptions/{id}/trigger'

class CreateSubscription(Request):

    uri = 'emails/subscriptions'

    def clean_uri(self):

        return 'emails/subscriptions'

class LinkTemplate(Request):

    uri = '/emails/subscriptions/{id}/templates/{template_id}'

    resource = EmailSubscriptionTemplate

    def clean_uri(self):

        return '/emails/subscriptions/{id}/templates/{template_id}'
