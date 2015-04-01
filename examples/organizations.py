from pysis import SIS

if __name__ == "__main__":
    s = SIS(token="f03109ef580328e3a24cbb611d84c92fc8758b60")
    
    org = s.organizations.get(1)
    
    print("\nFacilities \n---------")
    data = org.getFacilities()
    for fac in data:
        print(str(fac.id) + ' : ' + fac.name + ' : ' + fac.created_at)
    
    print("\nBuildings \n---------")
    data = org.getBuildings()
    for building in data:
        print(str(building.id) + ' : ' + building.label + ' : ' + building.created_at)
            
    print("\nUsers \n---------")
    data = org.getUsers()
    for user in data:
        print(str(user.id) + ' : ' + user.first_name + ' : ' + user.created_at)
        
    print("\nFeeds \n---------")
    data = org.getFeeds()
    for feed in data:
        print(str(feed.id) + ' : ' + feed.key + ' : ' + feed.created_at)
        
    print("\nOutputs \n---------")
    data = org.getOutputs()
    for output in data:
        print(str(output.id) + ' : ' + output.label + ' : ' + output.created_at) 
        
    print("\nBlastcells \n---------")
    data = org.getBlastcells()
    for blastcell in data:
        print(str(blastcell.id) + ' : ' + blastcell.label + ' : ' + blastcell.created_at) 
    
