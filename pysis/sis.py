#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class SIS(object):
    __BASE_URL__ = 'https://api.ndustrial.io/v1/'
    __API_DOMAIN__ = 'api.ndustrial.io'



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
        
        enableParamChecks = True
        if 'enableParamChecks' in config:
            enableParamChecks = config['enableParamChecks']          
        
        Resource.setParamCheck(enableParamChecks)
        
        if 'token' not in config:
            raise ValueError("token must be passed in. ex- SIS(token='xyz...')")
        
        if 'api_domain' not in config:
            config['api_domain'] = self.__API_DOMAIN__
        
        if 'base_url' not in config:
            config['base_url'] = self.__BASE_URL__
            
        self._client = Client(**config)
        
        self._organizations = Organizations(self._client)
        self._facilities = Facilities(self._client)
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
    
if __name__ == "__main__":
    s = SIS(token="4d324dd24781f122e7a5d71579ef599a2e345916")

    # print('Getting all active alerts..')
    #
    # alert = s.alerts.get(is_active=True)
    #
    # for a in alert:
    #
    #     print(a.id)
    #
    # print('Getting all alerts..')
    #
    # alert = s.alerts.get()
    #
    # for a in alert:
    #
    #     print(a.id)
    #
    #
    # print('Triggering alert ff941406-7edc-436b-b5e9-803a5635f21b...')
    #
    #
    # s.alerts.trigger('ff941406-7edc-436b-b5e9-803a5635f21b', {"data":"test"})
    #
    # feedTypes = s.feeds.getTypes();
    #
    # for t in feedTypes:
    #     print(t.type + ": " + str(t.down_after));

    response = s.alerts.create(alert={'alert_type_id': 1,
                                      'label': 'Created from python',
                                      'is_active': True,
                                      'facility_id': 66})

    print(str(response))



    
    
