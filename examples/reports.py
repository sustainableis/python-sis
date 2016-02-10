from pysis import SIS

s = SIS(token="c3c77c8f276f6d33be9c31f2aa4529b2fca482d4", base_url='http://api.sustainableis.com/v1/', api_domain='api.sustainableis.com')

print("\Reports (All) \n---------")

reports = s.reports.getAllReportTypes()
print reports

