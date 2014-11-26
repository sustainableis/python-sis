Documentation Overview
=======================

**pysis** is a SIS APIv1 python wrapper.

You can consume the API with several :doc:`pysis.services` (organizations, outputs...) like
you see in `http://docs.sisdataversion2.apiary.io/`.

When you do an API request, it will return :doc:`pysis.resources`
which can do its own related requests.

Sample
------
::
	from pysis import SIS

	s = SIS(token="<insert token here")

	org = s.organizations.get(1)

	print("\nFacilities \n---------")
	data = org.getFacilities()
	#data = [<Facility (facility_id=1)>, <Facility (facility_id=4)>]

	for fac in data:
		print(str(fac.id) + ' : ' + fac.name + ' : ' + fac.created_at)

TOC
------
.. toctree::
    :maxdepth: 3

    pysis.services
    pysis.resources

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
