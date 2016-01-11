from pysis.services.base import Service
from uuid import UUID

class Emails(Service):
    """Emails Service

    Consumes Emails API: <{url}/emails>
    """
    def __init__(self, client):
        """Creates Emails object with a client"""
        super(Emails, self).__init__(client)

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

            request = self.request_builder('emails.getSubscriptions', **params)

        else:

            # try-parse UUID
            try:
                u = UUID(id);
            except ValueError:

                print('id must be a valid UUID')

                return

            request = self.request_builder('emails.getSubscriptions', id=id)

        return self._get(request)

    def createSubscription(self, subscription):

        request = self.request_builder('emails.createSubscription', body=subscription)

        return self._post(request)


    def triggerSubscription(self, id, data):

        # try-parse UUID
        try:
            u = UUID(id);
        except ValueError:

            print('id must be a valid UUID')

            return

        request = self.request_builder('emails.triggerSubscription', id=id, body=data)

        return self._post(request)
