# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Outputs(Service):
    """ 
    Consume `Outputs API <http://api.sustainableis.com/v1/outputs>`_ 
    
    Example uses:
    ------------
    TODO
    s.organizations.create({'name': 'Sample Organization'})
    org = s.organizations.get(id=30)
    s.organizations.update(30, {'name': 'Org Name'})
    s.organizations.delete(30)
    """

    def __init__(self, client):
        super(Outputs, self).__init__(client)
    
    def get(self, id=None, 
            type=None, category=None, feed_id=None, 
            building_id=None, facility_id=None, organization_id=None):
        """ Get a specific output or all of them if id=None
            
            Apply a filter if one is given.
        :returns A :doc:`response`
        """
        
        _filterDict = {}
        _filterDict['type'] = type
        _filterDict['category'] = category
        _filterDict['feed_id'] = feed_id
        _filterDict['building_id'] = building_id
        _filterDict['facility_id'] = facility_id
        _filterDict['organization_id'] = organization_id
        
        #Check for a filter, but only allow one
        filterName = None
        filterValue = None
                
        for filter, value in _filterDict.items():
            if value is not None:
                if filterName is not None:
                    #only 1 filter at a time
                    raise ValueError('Only one filter can be used at a time')
                else:
                    filterName, filterValue = filter, value        
        
        if id is None:
            request = self.request_builder('outputs.get', filterName=filterName, filterValue=filterValue)
        else:
            assert isinstance(id, int)
            request = self.request_builder('outputs.get', id=id, filterName=filterName, filterValue=filterValue)
            
        return self._get(request)
    
    def getFields(self, id):
        """ Get all of the fields for an output
        
        :returns A :doc:`response`
        """
        assert isinstance(id, int)
        request = self.request_builder('outputs.getFields', id=id)
        return self._get(request)
    
    def getRefrigerationData(self, id):
        """ Get the refrigeration data of an output
        
        :returns A :doc:`response`
        """
        assert isinstance(id, int)
        request = self.request_builder('outputs.getRefrigerationData', id=id)
        return self._get(request)
        
        
        