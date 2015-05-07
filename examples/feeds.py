from pysis import SIS

s = SIS(token="1bb9d1ea3e31d3908ba35577d73d9718377dab95")

print("\nFeeds (Examples) \n---------")

feed = s.feeds.get(id=90)
print feed.id, feed.key

feeds = s.feeds.get(key='ngest-santa-maria-logix')
for feed in feeds:
    print feed.id, feed.key, feed.facility_id
    for config in feed.getConfigurations():
        print config.title, config.environment
    for value in feed.getConfigurationValues(environment='development'):
        print value.type, value.key, value.value