# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Users(Service):
    """Users Service
    
    Consumes Users API: <{url}/users>    
    """

    def __init__(self, client):
        """Creates Users object with a client"""
        super(Users, self).__init__(client)
    
    def get(self, id=None):
        """Gets Users from the API
        
        Args:
            id (int): id of the user. 
                if None, returns all Users
        
        Returns: Users resources        
        """
        if id is None:
            request = self.request_builder('users.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('users.get', id=id)
            
        return self._get(request)
    