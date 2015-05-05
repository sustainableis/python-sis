from pysis import SIS

s = SIS(token="4eeb61e2cac55f77e6402df50e105b1923255a79")

print("\nConfigurations (All) \n---------")

worker = s.workers.get(uuid="d91adc8c-8961-907d-4478-019da1b2d483")
print worker.uuid, worker.label

configs = worker.getConfigurations()
for config in configs:
  print config.environment,config.title,config.description

prod_configs = worker.getConfigurations(environment='development')
for config in prod_configs:
  print 'DEV: %s %s'%(config.environment, config.title)

config_values = worker.getConfigurationValues(environment='production')
for value in config_values:
    print value.type, value.key, value.value