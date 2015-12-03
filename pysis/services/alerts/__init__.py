from pysis.services.base import Service
from uuid import UUID

class Alerts(Service):
    """Alerts Service

    Consumes Alerts API: <{url}/alerts>
    """

    def __init__(self, client):
        """Creates Alerts object with a client"""
        super(Alerts, self).__init__(client)

    def get(self, id=None, facility_id=None, is_active=None):
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

            request = self.request_builder('alerts.get', **params)

        else:

            # try-parse UUID
            try:
                u = UUID(id);
            except ValueError:

                print('id must be a valid UUID')

                return

            request = self.request_builder('alerts.get', id=id)

        return self._get(request)


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

            print('id must be a valid UUID')

            return

        request = self.request_builder('alerts.trigger', id=id)

        return self._post(request, data);