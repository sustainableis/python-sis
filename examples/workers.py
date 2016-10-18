from pysis import SIS

s = SIS(token="1bb9d1ea3e31d3908ba35577d73d9718377dab95")

print("\nConfigurations (All) \n---------")

worker = s.workers.get(uuid="f2f8d08a-8be7-8fbc-5157-9950c92497b7")
print (worker.uuid, worker.label)

configs = worker.getConfigurations()
for config in configs:
  print (config.environment,config.title,config.description)

prod_configs = worker.getConfigurations(environment='development')
for config in prod_configs:
  print ('DEV: %s %s'%(config.environment, config.title))

config_values = worker.getConfigurationValues(environment='production')
for value in config_values:
    print (value.type, value.key, value.value)
