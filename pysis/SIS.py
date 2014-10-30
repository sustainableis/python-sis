#!/usr/bin/env python
# -*- encoding: utf-8 -*-

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
        
        if 'token' not in config:
            raise ValueError("token must be passed in. ex- SIS(token='xyz...')")
        
        if 'api_domain' not in config:
            config['api_domain'] = self.__API_DOMAIN__
        
        if 'base_url' not in config:
            config['base_url'] = self.__BASE_URL__
        
        self._organizations = Organizations(**config)

    @property
    def organizations(self):
        return self._organizations
        
if __name__ == "__main__":
    s = SIS(token="1a765a554a2359feb69c62b8b73576376c236fca")
    data = s.organizations.get()
    for org in data:
        print(str(org.id) + ' : ' + org.name + ' : ' + org.created_at)
        
    print("---------\n")
    org1 = s.organizations.get(id=1)
    print(str(org1.id) + ' : ' + org1.name + ' : ' + org1.created_at)
