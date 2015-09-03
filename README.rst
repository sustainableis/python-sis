# pySIS

## Installation

To install pySIS, simply run:
  
    python setup.py install

With superuser permissions. 


## nGest

### Background

**nGest** is a piece of software that enables time-series data to be brought into the ndustrial.io backend in a flexible way. Time-series data is a stream of data points paired with timestamps, although it is not necessary that the data be in time order. 

To understand nGest, it is important to understand two concepts about the backend:

- Organization of Data Sources in the Backend

Data sources are organized according to three concepts: feeds, outputs, and fields.

A feed is a stream of data. It generally comes from a single physical device.  A feed contains one or more outputs.  When you want to put data into the ndustrial.io backend, you are assigned one or more feeds. 

An output is a source of data.  An output contains one or more fields.  It may be physical, in which case an output and a feed can be thought of the same way.  An output can also be logical, that is, created by some combination of true physical outputs. An example of an output is a combined temperature/humidity sensor.  The temperature/humidity sensor would be a data source within an associated feed.  

A field is a particular facet of data coming from an output.  In the example above, the combined temperature/humidity sensor would have two fields: temperature, and humidity.  Outputs can contain many fields.  An energy measurement output may contain fields for voltage, current, power, power-factor, etc. Fields have a type (string, numeric, boolean) and units (degrees, kW, kWh, etc) where applicable. 


- The concept/system of "workers"

Workers are pieces of Python code that are run periodically.  Workers interface with your databases, read text files, or otherwise interface with data sources as needed, and workers make use of nGest to send data to ndustrial.io.  Workers are identified with a unique ID and have configuration data stored in the </ndustrial.io> backend.  

nGest can be backed by any data source: a sensor, a database, text files, anything that collects or reports time-series data. nGest is a first-class feed type in the ndustrial.io backend, and we work with you to provision outputs and fields to support your nGest feed as necessary. 

 
### Usage

Import the nGest library with:

    from workertools.ngest import NgestClient
    from workertools.ngest import NgestTimeSeriesDataObject
    from workertools.ngest import NonUniqueFieldIDException


Next, create an nGest client using your feedKey (usually stored in the worker config)

    self.feedKey = self.config['feed_key']

    self.nGestClient = NgestClient(self.feedKey)


Next, create an NgestTimeSeriesDataObject with your feed key, and add data to it with the pre-provisioned field id

    field_id = "example_worker_field"

    nGestObject = NgestTimeSeriesDataObject(self.feedKey);

    # timestamp, field id, value
    nGestObject.addTimeValue('2015-09-03 12:00:00', field_id, 55);


Add as much data as you need to, then send it with:

    self.nGestClient.sendData(nGestObject)



For the full example, check out workertools/exampleworker.py in the pysis folder.
