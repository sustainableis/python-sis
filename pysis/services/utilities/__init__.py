# -*- encoding: utf-8 -*-

from pysis.services.base import Service
from uuid import UUID

class Utilities(Service):
    """ Utilities Service
    """

    def __init__(self, client):
        """Creates Utility object with a client"""
        super(Utilities, self).__init__(client)
    
    def getMeters(self, id=None, building_id = None):
        """Gets Meters from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Meters
        
        Returns: Utility resources      
        """
        if id:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getMeters', id=id)
        elif building_id:
            assert isinstance(building_id, int)
            request = self.request_builder('utilities.getMeters', building_id=building_id)
        else:
            request = self.request_builder('utilities.getMeters')
            
        return self._get(request)
    
    def getAccounts(self, id=None):
        """Gets Accounts from the API
        
        Args:`
            id (int): id of the feed. 
                if None, returns all Accounts
        
        Returns: Utility resources      
        """
        if id is None:
            request = self.request_builder('utilities.getAccounts')
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getAccounts', id=id)
            
        return self._get(request)
        
    def getStatements(self, id=None, meter_id=None):
        """Gets Statements from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Statements
        
        Returns: Utility resources      
        """
        if id:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getStatements', id=id)
        elif meter_id:
            assert isinstance(meter_id, int)
            request = self.request_builder('utilities.getStatements', meter_id=meter_id)
        else:
            request = self.request_builder('utilities.getStatements')
            
        return self._get(request)

    def getStatementTree(self, id=None):
        """Gets Statements from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Statement trees
        
        Returns: Utility resources      
        """
        if id is None:
            request = self.request_builder('utilities.getStatementTree')
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getStatementTree', id=id)
            
        return self._get(request)

    def getStatementHistory(self, id=None):
        """Gets Statements from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Statement trees
        
        Returns: Utility resources      
        """
        if id is None:
            request = self.request_builder('utilities.getStatementHistory')
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getStatementHistory', id=id)
            
        return self._get(request)

    def setStatement(self, id = None, data = None):
        '''
            pass data as a JSON object
        '''
        if id is None:
            print("id must be valid")
            return
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.setStatement', id=id, body = data)

        return self._put(request)

    def setMeter(self, id = None, data = None):
        '''
            pass data as a JSON object
        '''
        if id is None:
            print("id must be valid")
            return
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.setMeter', id=id, body = data)

        return self._put(request)









