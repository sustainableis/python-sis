# -*- encoding: utf-8 -*-

from pysis.services.base import Service
from datetime import datetime

class Outputs(Service):
    """Outputs Service
    
    Consumes Outputs API: <{url}/outputs>    
    """

    def __init__(self, client):
        """Creates Outputs object with a client"""
        super(Outputs, self).__init__(client)
    
    def get(self, id=None, 
            type=None, category=None, feed_id=None, 
            building_id=None, facility_id=None, organization_id=None):
        """Get a specific output or all of them if id=None
        
        Apply a filter if one is given.
        Only 1 filter can be used at a time!
        
        Args:
            id (int): id of the output.
            type (str): Filter - if used, will get a list of outputs of the given type
            category (str): Filter - if used, will get a list of outputs of the given category
            feed_id (int): Filter - if used, will get a list of outputs with the given feed_id
            building_id (int): Filter - if used, will get a list of outputs with the given building_id
            facility_id (int): Filter - if used, will get a list of outputs with the given facility_id
            organization_id (int): Filter - if used, will get a list of outputs with the given organization_id
            
        Returns: 
            Fields resources  
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
        """Get all the fields for an output
        
        Args:
            id (int): id of the output.
            
        Returns: 
            Fields resources  
        """
        assert isinstance(id, int)
        request = self.request_builder('outputs.getFields', id=id)
        return self._get(request)
    
    def getData(self, id, timeStart=None, timeEnd=None, window=None, field=""):
        """Get the data of an output
        
        Args:
            id (int): id of the output.
            timeStart (datetime or None): start time of the data
            timeEnd (datetime or None): end time of the data
            window (int): window of data in seconds
            field (str): field_human_name filter 
            
        Returns: 
            Data resources  
        """
        assert isinstance(id, int)
        assert isinstance(timeStart, (datetime, type(None)))
        assert isinstance(timeEnd, (datetime, type(None)))
        assert isinstance(window, (int, type(None)))
        assert isinstance(field, str)
        
        if timeStart is not None: 
            timeStart = int((timeStart - datetime(1970,1,1)).total_seconds())
        if timeEnd is not None: 
            timeEnd = int((timeEnd - datetime(1970,1,1)).total_seconds())
        
        request = self.request_builder('outputs.getData', 
                                       id=id,
                                       timeStart=timeStart, 
                                       timeEnd=timeEnd, 
                                       window=window, 
                                       field=field)
        return self._get(request)


    def getMetrics(self, id, field, metric_name, timeStart=None, timeEnd=None):

        assert isinstance(timeStart, (datetime, type(None)))
        assert isinstance(timeEnd, (datetime, type(None)))

        if timeStart is not None:
            timeStart = int((timeStart - datetime(1970,1,1)).total_seconds())
        if timeEnd is not None:
            timeEnd = int((timeEnd - datetime(1970,1,1)).total_seconds())
        
        request = self.request_builder('outputs.getMetrics',
                                       id=id,
                                       field=field,
                                       metric_name=metric_name,
                                       timeStart=timeStart,
                                       timeEnd=timeEnd)

        return self._get(request)