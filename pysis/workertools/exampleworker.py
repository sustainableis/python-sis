from workertools.ngest import NgestClient
from workertools.ngest import NgestTimeSeriesDataObject
from workertools.ngest import NonUniqueFieldIDException
from workertools.baseworker import BaseWorker
from datetime import datetime



# this is the unique identifier for this worker
WORKER_UUID = '62b76408-c3ce-61be-8d27-b8f8aba73b72'


# ExampleWorker is a class that is based on BaseWorker
class ExampleWorker(BaseWorker):

	# this constructor initializes the ExampleWorker class
	def __init__(self):

		# call BaseWorker's constructor to pull configurations
		# from the SIS api.  This will tell our worker what databases
		# to look in, which feed key to use, etc
		super(ExampleWorker, self).__init__(WORKER_UUID, "staging")

		# this is the nGest feed key that was pulled from configuration
		self.feedKey = self.config['feed_key']

		# initialize an NgestClient using the feed key.  This will send data
		# to the SIS servers for us.  
		self.nGestClient = NgestClient(self.feedKey)


	# in this worker, we are going to get data from a simple text file not unlike
	# the files Len's code has been generating.  Each line of the file will
	# contain a data point and a timestamp in ISO format separated by a comma
	# e.g. 415.6,2015-06-15 21:15:00
	def doWork(self):

		# this field ID has to actually be created in the ndustrial.io system.. 
		# it can be anything that is descriptive of the data it represents
		field_id = "example_worker_field"

		# Name of the file.  It would be fairly easy to create an array of files from
		# all the files in a folder, for example. But for now, just use one. 
		fileName = "test.txt"

		# this NgestTimeSeriesDataObject will hold the data that we are going
		# to send to SIS
		nGestObject = NgestTimeSeriesDataObject(self.feedKey);

		# open the file, and capture an object 'lines' that is a list of all the
		# lines in the file. 
		with open(fileName) as f:
		    lines = f.readlines()


		# Now loop through each line in the file, and add the data to 
		# nGest.  Note that everything after the next statement that is
		# similarly indented will be considered part of the loop. 
		for line in lines:

			# spit the data.  the resulting list will contain
			# 2 entries.  
			data = line.split(',')

			# this is the value, everything before the comma
			value = data[0]

			# this is the timestamp, everything after the comma
			# this is still in string form, we will convert it 
			# to a datetime value 
			t = data[1]

			print 'Sending ' + timestamp + ': ' + value;

			# convert string representation of timestamp to datetime object
			# the second argument tells python how to interperent the string
			# %Y = year (2015, etc)
			# %m = zero-padded month (04, 05, etc)
			# %d = zero-padded day (12, 31, etc)
			# %H = zero-padded hour, 24 hour clock (01, 22, etc)
			# %M = zero-padded minute (03, 04, 05, etc)
			# %S = zero-padded second (11, 12, 13, etc)
			timestamp = strptime(t, "%Y-%m-%d %H:%M:%S")

			# we now have everything we need to add the data to nGest!
			nGestObject.addTimeValue(timestamp, field_id, data[0])

			# loop to the next line in the file


		# now that all values have been added to the NgestTimeSeriesDataObject, 
		# we can ask the nGestClient we set up in the __init__ method to send it for
		# us. 
		self.nGestClient.sendData(nGestObject)


