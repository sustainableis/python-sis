# -*- encoding: utf-8 -*-

from pysis.services.base import Service

class Organizations(Service):
    """Organizations Service
    
    Consumes Organizations API: <{url}/organizations>    
    """

    def __init__(self, client):
        """Creates Organizations object with a client"""
        super(Organizations, self).__init__(client)
    
    def get(self, id=None):
        """Gets Organizations from the API
        
        Args:
            id (int): id of the organization. 
                if None, returns all Organizations
        
        Returns: 
            Organizations resources        
        """
        if id is None:
            request = self.request_builder('organizations.get')
        else:
            assert isinstance(id, int)
            request = self.request_builder('organizations.get', id=id)
            
        return self._get(request)
    
    def create(self, data):
        """Create an Organization
        
        Args:
            data (dict): {'name': 'Sample Organization'}
        
        Returns: 
            Response 
        """
        #TODO: Make sure name is not '' if the node server doesn't
        request = self.request_builder('organizations.create', body=data)
        return self._post(request)
    
    def delete(self, id):
        """Delete an Organization
        
        Args:
            id (int): id of the organization.  
            
        Returns: 
            Response  
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.delete', id=id)
        return self._delete(request)
    
    def update(self, id, data):
        """Create an Organization
        
        Args:
            id (int): id of the organization.
            data (dict): {'name': 'Sample Organization'}
            
        Returns: 
            Resource
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.update', id=id, body=data)
        return self._put(request)
        
    def getFacilities(self, id):
        """Get the facilities of an organization
        
        Args:
            id (int): id of the organization.  
            
        Returns: 
            Facilities resources  
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.getFacilities', id=id)
        return self._get(request)
    
    def getBuildings(self, id):
        """Get the buildings of an organization
        
        Args:
            id (int): id of the organization.  
            
        Returns: 
            Buildings resources   
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.getBuildings', id=id)
        return self._get(request)
    
    def getUsers(self, id):
        """Get the users of an organization
        
        Args:
            id (int): id of the organization.    
            
        Returns: 
            Users resources 
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.getUsers', id=id)
        return self._get(request)
    
    def getFeeds(self, id):
        """Get the feeds of an organization
        
        Args:
            id (int): id of the organization. 
            
        Returns: 
            Feeds resources    
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.getFeeds', id=id)
        return self._get(request)
    
    def getOutputs(self, id):
        """Get the outputs of an organization
        
        Args:
            id (int): id of the organization. 
            
        Returns: 
            Outputs resources    
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.getOutputs', id=id)
        return self._get(request)
    
    def getBlastcells(self, id):
        """Get the blastcells of an organization
        
        Args:
            id (int): id of the organization.    
            
        Returns: 
            Blastcells resources 
        """
        assert isinstance(id, int)
        request = self.request_builder('organizations.getBlastcells', id=id)
        return self._get(request)
    
        
        