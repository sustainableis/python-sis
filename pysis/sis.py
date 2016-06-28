#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from datetime import datetime
import calendar

class SIS(object):
    #__BASE_URL__ = 'http://api.sustainableis.com/v1/'
    #__API_DOMAIN__ = 'api.sustainableis.com'
    __BASE_URL__ = 'http://localhost:3000/v1/'
    __API_DOMAIN__ = 'localhost:3000'



    """Main SIS object
    
    You can configure all services globally using the config dict.
    See the attributes in `pysis.core.client`.

    Examples:
        s = SIS(token='xyz...')
        s = SIS(token='xyz...', base_url='http://api.sustainableis.com/v2/')
        s = SIS(token='xyz...', enableParamChecks=False)
    """

    def __init__(self, **config):
        from pysis.core.client import Client
        from pysis.resources.base import Resource

        from pysis.services.organizations import Organizations
        from pysis.services.facilities import Facilities
        from pysis.services.utilities import Utilities
        from pysis.services.outputs import Outputs
        from pysis.services.buildings import Buildings
        from pysis.services.feeds import Feeds
        from pysis.services.users import Users
        from pysis.services.blastcells import Blastcells
        from pysis.services.weather import Weather
        from pysis.services.configurations import Configurations
        from pysis.services.oauth import Oauth
        from pysis.services.workers import Workers
        from pysis.services.alerts import Alerts
        from pysis.services.emails import Emails
        from pysis.services.reports import Reports
        from pysis.services.metrics import Metrics
        
        enableParamChecks = True
        if 'enableParamChecks' in config:
            enableParamChecks = config['enableParamChecks']          
        
        Resource.setParamCheck(enableParamChecks)
        
        if 'api_domain' not in config:
            config['api_domain'] = self.__API_DOMAIN__
        
        if 'base_url' not in config:
            config['base_url'] = self.__BASE_URL__
            
        self._client = Client(**config)
        
        self._organizations = Organizations(self._client)
        self._facilities = Facilities(self._client)
        self._utilities = Utilities(self._client)
        self._outputs = Outputs(self._client)
        self._buildings = Buildings(self._client)
        self._feeds = Feeds(self._client)
        self._users = Users(self._client)
        self._blastcells = Blastcells(self._client)
        self._weather = Weather(self._client)
        self._configurations = Configurations(self._client)
        self._oauth = Oauth(self._client)
        self._workers = Workers(self._client)
        self._alerts = Alerts(self._client)
        self._emails = Emails(self._client)
        self._reports = Reports(self._client)
        self._metrics = Metrics(self._client)

    @property
    def organizations(self):
        return self._organizations
    
    @property
    def facilities(self):
        return self._facilities
    
    @property
    def outputs(self):
        return self._outputs
    
    @property
    def buildings(self):
        return self._buildings
    
    @property
    def users(self):
        return self._users
    
    @property
    def feeds(self):
        return self._feeds
    
    @property
    def blastcells(self):
        return self._blastcells
    
    @property
    def weather(self):
        return self._weather
    
    @property
    def configurations(self):
        return self._configurations
    
    @property
    def oauth(self):
        return self._oauth
    
    @property
    def workers(self):
        return self._workers

    @property
    def alerts(self):
        return self._alerts

    @property
    def emails(self):
        return self._emails

    @property
    def reports(self):
        return self._reports

    @property
    def utilities(self):
        return self._utilities

    @property
    def metrics(self):
        return self._metrics
    
    
