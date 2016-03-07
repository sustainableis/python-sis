from pysis import SIS


if __name__ == "__main__":

	'''
	  "token_type": "bearer",
	  "access_token": "af2f907ac7dc4348393fd9a63c25cd90f6852d2a",
	  "expires_in": 2678400,
	  "refresh_token": "81c625d1cb6c79cc06fab35d59be1f922b294803"
	'''
	'''
	#stage
	s = SIS(token="c3c77c8f276f6d33be9c31f2aa4529b2fca482d4", base_url='http://api.sustainableis.com/v1/', api_domain='api.sustainableis.com')
	'''

	#prod
	s = SIS(token="af2f907ac7dc4348393fd9a63c25cd90f6852d2a", base_url='http://api.ndustrial.io/v1/', api_domain='api.ndustrial.io')


	print("\Reports (All) \n---------")

	
	reports = s.reports.getAllReportTypes()
	print reports

	report_type = s.reports.getReportType('4e72b0ca-b5d1-44cd-9851-2213c67fde62')
	print report_type

	fac=65

	report = s.reports.getReportByFacID(report_type.id, fac)
	s.reports.createFacilityReport(fac, report[0].id)
	subscription = s.emails.createSubscription(subscription = {"name": "Test", "description": "Test", "type": "Report"})
	print subscription.id
	s.reports.addSubscriptionToReport(rid = report[0].id, sid = subscription.id)
	gen_report = s.reports.createGeneratedReport(rid = report[0].id, data = "")
	s.reports.addAttachmentToGenerateReport(gid = gen_report.id, data = {"file_id": 8})
	s.reports.triggerSubscription(gid = gen_report.id)