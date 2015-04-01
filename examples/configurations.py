from pysis import SIS

if __name__ == "__main__":
    s = SIS(token="f03109ef580328e3a24cbb611d84c92fc8758b60")
    
    print("\nConfigurations (All) \n---------")
    configs = s.configurations.get()
    for config in configs:
        print("%s : %s : %s : %s : %s : %s" % (config.id, config.environment, config.title, config.description, config.created_at, config.updated_at))
        
    #print("\nConfigurations (22) \n---------")
    #config = s.configurations.get(22)
    #print(str(config.id) + ' : ' + config.environment + ' : ' + config.title + ' : ' + config.description + ' : ' + config.created_at + ' : ' + config.updated_at)
    
    #print("\nConfigurations Create \n---------")
    #config = s.configurations.create({'environment': 'development', 'title' : 'pysis test'}) #, 'description' : 'desc' })
    #print(config)
    
    #config = s.configurations.update(52, {'environment': 'development', 'title' : 'pysis test', 'description' : 'updatedDesc'})
    #print("%s : %s : %s : %s : %s : %s" % (config.id, config.environment, config.title, config.description, config.created_at, config.updated_at))
    
    #for i in range(52, 60):
    #    s.configurations.delete(i)
    