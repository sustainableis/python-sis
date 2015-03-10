# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Oauth(Service):
    """OAuth Service
    
    Consumes OAuth API: <{url}/oauth>    
    """

    def __init__(self, client):
        """Creates OAuth object with a client"""
        super(Oauth, self).__init__(client)
            
    def refreshToken(self, client_id='', client_secret='', refresh_token=''):
        """Refresh the OAuth token of a user
        
        Args:
            client_id (str): client id string.
            client_secret (str): secret string for a client
            refresh_token (str): refresh token used to create a new access_token
            
        Returns: 
            OAuth Resource
        """
        assert isinstance(client_id, str)
        assert isinstance(client_secret, str)
        assert isinstance(refresh_token, str)
        
        formData = {'grant_type' : 'refresh_token',
                   'client_id' : client_id,
                   'client_secret' : client_secret,
                   'refresh_token' : refresh_token
                   }
        
        request = self.request_builder('oauth.refreshToken', body=formData) 
        return self._post(request, headers={'content-type' : 'application/x-www-form-urlencoded'})        
        