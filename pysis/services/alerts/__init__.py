from pysis.services.base import Service
from uuid import UUID
import datetime
import pytz

class Alerts(Service):
    """Alerts Service

    Consumes Alerts API: <{url}/alerts>
    """

    def __init__(self, client):
        """Creates Alerts object with a client"""
        super(Alerts, self).__init__(client)

    def get(self, id=None, facility_id=None, is_active=None, alert_type_id=None):
        """Gets Alerts from the API

        Args:
            id (string): id of the alert.
                if None, returns all alerts
            facility_id (int): facility of the alert(s)
            is_active (boolean): active status of alert

        Returns: Alert resources
        """
        if id is None:

            params = {}
            if facility_id:
                params['facility_id'] = facility_id

            if is_active:
                params['is_active'] = is_active

            if alert_type_id:
                params['alert_type_id'] = alert_type_id

            request = self.request_builder('alerts.get', **params)

        else:

            # try-parse UUID
            try:
                u = UUID(id);
            except ValueError:

                raise Exception('id must be a valid UUID')


            request = self.request_builder('alerts.get', id=id)

        return self._get(request)


    def create(self, alert):

        request = self.request_builder('alerts.create', body=alert)

        return self._post(request)


    def trigger(self, id, data):
        """Triggers an alert

        Args:
            id (string): id of the alert.
            data (dict): payload to deliver with alert

        Returns: Nothing
        """
        # try-parse UUID
        try:
            u = UUID(id);
        except ValueError:

            raise Exception('id must be a valid UUID')

        request = self.request_builder('alerts.trigger', id=id, body=data)

        return self._post(request)


    def getEmailSubscriptions(self, id=None):

        if id is None:

            request = self.request_builder('alerts.getEmailSubscriptions')

        else:
            # try-parse UUID
            try:
                u = UUID(id);
            except ValueError:

                raise Exception('id must be a valid UUID')

                return

            request = self.request_builder('alerts.getEmailSubscriptions', id=id)

        return self._get(request)


    def linkEmailSubscription(self, id, email_subscription_id):

        if id is not None:

            # try-parse UUID
            try:
                u = UUID(id);
            except ValueError:

                raise Exception('Provided alert_id must be a valid UUID')

                return
        else:

            raise Exception('Request must include alert_id!')

        if email_subscription_id is not None:

            # try-parse UUID
            try:
                u = UUID(id);
            except ValueError:

                raise Exception('Provided email_subscription_id must be a valid UUID')

        else:

            raise Exception('Request must include email_subscription_id!')

        request = self.request_builder('alerts.linkEmailSubscription', id=id, email_subscription_id=email_subscription_id)

        return self._post(request)

    def getTriggeredAlerts(self, alert_id, timeStart=None, timeEnd=None):

         # try-parse UUID
        try:
            u = UUID(alert_id);
        except ValueError:

            raise Exception('Provided alert_id must be a valid UUID')


        params = {'id': alert_id}

        if timeStart is not None:

            assert isinstance(timeStart, datetime.datetime)

            # delocalize if necessary
            if timeStart.tzinfo is not None:
                timeStart = timeStart.astimezone(pytz.utc)

            timeStart = timeStart.strftime('%Y-%m-%dT%H:%M:%S')

            params['timeStart'] = timeStart

            if timeEnd is not None:

                assert isinstance(timeEnd, datetime.datetime)

                # delocalize if necessary
                if timeEnd.tzinfo is not None:
                    timeEnd = timeEnd.astimezone(pytz.utc)

                timeEnd = timeEnd.strftime('%Y-%m-%dT%H:%M:%S')

                params['timeEnd'] = timeEnd



        request = self.request_builder('alerts.getTriggeredAlerts', **params)

        return self._get(request)