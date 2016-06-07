# -*- encoding: utf-8 -*-

from pysis.services.base import Service
from uuid import UUID

class Utilities(Service):
    """ Utilities Service
    """

    def __init__(self, client):
        """Creates Utility object with a client"""
        super(Utilities, self).__init__(client)
    
    def getMeters(self, id=None):
        """Gets Meters from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Meters
        
        Returns: Utility resources      
        """
        if id is None:
            request = self.request_builder('utilities.getMeters')
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getMeters', id=id)
            
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
        
    def getStatements(self, id=None):
        """Gets Statements from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Statements
        
        Returns: Utility resources      
        """
        if id is None:
            request = self.request_builder('utilities.getStatements')
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getStatements', id=id)
            
        return self._get(request)

    def getStatementsByMeterID(self, id=None):
        """Gets Statements from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Statements
        
        Returns: Utility resources      
        """
        if id is None:
            request = self.request_builder('utilities.getStatementsByMeterID')
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getStatementsByMeterID', id=id)
            
        return self._get(request)

    def getMetersByBuildingID(self, id=None):
        """Gets Statements from the API
        
        Args:
            id (int): id of the feed. 
                if None, returns all Statements
        
        Returns: Utility resources      
        """
        if id is None:
            request = self.request_builder('utilities.getMetersByBuildingID')
        else:
            assert isinstance(id, int)
            request = self.request_builder('utilities.getMetersByBuildingID', id=id)
            
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









