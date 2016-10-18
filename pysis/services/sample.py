
from pysis import SIS
s = SIS(base_url='http://api.sustainableis.com/v1/', api_domain='api.sustainableis.com')
results = s.utilities.getStatements(meter_id = 2255)
print(str(results))
