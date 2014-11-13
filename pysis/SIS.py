#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pysis.core.client import Client
from pysis.resources.base import Resource

class SIS(object):
    __BASE_URL__ = 'http://api.sustainableis.com/v1/'
    __API_DOMAIN__ = 'api.sustainableis.com'
    
    """
    You can preconfigure all services globally with a ``config`` dict. See
    :attr:`~pysis.services.base.Service`

    Example::

        s = SIS(token='xyz...')
    """

    def __init__(self, **config):
        from pysis.services.organizations import Organizations
        from pysis.services.facilities import Facilities
        from pysis.services.outputs import Outputs
        from pysis.services.buildings import Buildings
        from pysis.services.feeds import Feeds
        from pysis.services.users import Users
        from pysis.services.blastcells import Blastcells
        
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
    
    
if __name__ == "__main__":
    s = SIS(token="5a417545a40bb6fd627ba3b05929843b6f4bf520")
    data = s.organizations.get()
    for org in data:
        print(str(org.id) + ' : ' + org.name + ' : ' + org.created_at)
        
    print("---------\n")
    org1 = s.organizations.get(id=30)
    print(str(org1.id) + ' : ' + org1.name + ' : ' + org1.created_at)
    
    print("---------")
    print("---------\n")
    
    data = s.facilities.get()
    for fac in data:
        print(str(fac.id) + ' : ' + fac.name + ' : ' + fac.created_at)
        
    print("---------\n")
    fac = s.facilities.get(id=30)
    print(str(fac.id) + ' : ' + fac.name + ' : ' + fac.created_at)
    
    print("---------")
    print("---------\n")
    
    data = s.organizations.getFacilities(1)
    for fac in data:
        print(str(fac.id) + ' : ' + fac.name + ' : ' + fac.created_at)
        
    org1 = s.organizations.get(1)
    data = org1.getFacilities()
    for fac in data:
        print(str(fac.id) + ' : ' + fac.name + ' : ' + fac.created_at)
        
    print("---------")
    print("---------\n")
    
    data = s.outputs.get()
    for output in data:
        print(str(output.id) + ' : ' + output.label + ' : ' + output.created_at)
       
    print("---------")
    print("---------\n")
     
    data = s.buildings.get()
    for output in data:
        print(str(output.id) + ' : ' + output.label + ' : ' + output.created_at)
        
    print("---------")
    print("---------\n")
     
    data = s.users.get()
    for output in data:
        print(str(output.id) + ' : ' + output.first_name + ' : ' + output.created_at)
        
    print("---------")
    print("---------\n")
     
    data = s.feeds.get()
    for feed in data:
        print(str(feed.id) + ' : ' + feed.key + ' : ' + feed.created_at)
        
    print("---------")
    print("---------\n")
     
    data = s.blastcells.get()
    for cell in data:
        print(str(cell.id) + ' : ' + cell.label + ' : ' + cell.created_at)
    
    #s.organizations.delete(26)
    #s.organizations.create({'name': 'Sample Organization'})
    
    
