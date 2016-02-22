from pysis import SIS


if __name__ == "__main__":

	
	#stage
	s = SIS(token="c3c77c8f276f6d33be9c31f2aa4529b2fca482d4", base_url='http://api.sustainableis.com/v1/', api_domain='api.sustainableis.com')
	

	'''
	#prod
	s = SIS(token="b9f01d7f50053da45d932a2e32a4bf87d9ae4f02", base_url='http://api.ndustrial.io/v1/', api_domain='api.ndustrial.io')
	'''

	print("\Reports (All) \n---------")

	report = s.reports.getReportType('3a22ba56-e695-43eb-8d70-53b54e66ce8c')
	print report
	
	reports = s.reports.getAllReportTypes()
	print reports

