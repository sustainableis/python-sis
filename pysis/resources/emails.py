

from .base import Resource

__service__ = 'Emails'

class EmailSubscription(Resource):

    def __str(self):
        return '<Emails>'

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
                    raise AttributeError(str(self.id), "Email must have id")
                return getattr(service, attr)(self.id)
            return wrapper
        else:
            raise AttributeError(attr)


class EmailSubscriptionTemplate(Resource):

    def __str(self):
        return '<Alerts>'

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
                    raise AttributeError(str(self.id), "Email must have id")
                return getattr(service, attr)(self.id)
            return wrapper
        else:
            raise AttributeError(attr)