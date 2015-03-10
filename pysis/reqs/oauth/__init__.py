# -*- encoding: utf-8 -*-

from pysis.reqs.base import Request
from pysis.resources.oauth import Oauth

class RefreshToken(Request):
    uri = 'oauth/token'
    resource = Oauth
    
    body_schema = {
                   'schema' : ('grant_type', 'client_id', 'client_secret', 'refresh_token'),
                   'required' : ('grant_type', 'client_id', 'client_secret', 'refresh_token') 
                  }
        

          
