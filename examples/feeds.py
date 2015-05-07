from pysis import SIS

s = SIS(token="1bb9d1ea3e31d3908ba35577d73d9718377dab95")

print("\nFeeds (Examples) \n---------")

feed = s.feeds.get(id=90)
print feed.id, feed.key

feeds = s.feeds.get(key='egauge6523')
for feed in feeds:
    print feed.id, feed.key, feed.facility_id

