#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class SIS(object):
    """
    You can preconfigure all services globally with a ``config`` dict. See
    :attr:`~pysis.services.base.Service`

    Example::

        s = SIS(token='xyz...')
    """

    def __init__(self, **config):
        from pysis.services.organizations import Organizations
        
        self._organizations = Organizations(**config)

    @property
    def organizations(self):
        return self._organizations
        
if __name__ == "__main__":
    s = SIS(token="1a765a554a2359feb69c62b8b73576376c236fca")
    data = s.organizations.getAll()
    for org in data:
        print(str(org.id) + ' : ' + org.name + ' : ' + org.created_at)
