from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from datetime import datetime
import collections



class CassandraUtility:

    def __init__(self, host, keyspace):

        self.cluster = Cluster([host])

        self.session = self.cluster.connect(keyspace=keyspace)


    def execute(self, query, args=None):

        statement = self.session.prepare(query)

        statement.consistency_level = ConsistencyLevel.TWO

        if args is not None:

            return self.session.execute(statement, args)

        else:

            return self.session.execute(statement)




    def getActiveOutputs(self, output_filter=None, field_filter=None):

        statement = 'SELECT output_id, event_time, field from output_data_by_field_latest'

        data = self.execute(statement)

        now = datetime.utcnow()

        # filter only recent data
        latestData = [ld for ld in data if (now-ld.event_time).days <= 5]


        # filter outputs
        if output_filter:
            latestData = [ld for ld in latestData if ld.output_id in output_filter]

        outputs = {}

        # if there is a field_filter, only include outputs containing fields from the
        # filter
        if field_filter:

            for ld in latestData:

                if ld.field in field_filter:

                    if ld.output_id not in outputs:
                        outputs[ld.output_id] = []

                    outputs[ld.output_id].append(ld.field)

        else:

            for ld in latestData:

                if ld.output_id not in outputs:
                    outputs[ld.output_id] = []

                outputs[ld.output_id].append(ld.field)


        return outputs


    def getData(self, output_id, field_human_name, time_start, window=0, time_end=None):

        if window == 0:

            table_name = 'output_data_by_field'

        elif window == 1:

            table_name = 'output_data_by_field_minutely'

        elif window == 15:

            table_name = 'output_data_by_field_15_minutely'

        elif window == 60:

            table_name = 'output_data_by_field_hourly'

        else:
            print 'Unknown window requested!!!'


        # get year from timestart.. currently dont support cross-year queries
        #timeStart = datetime.strptime(timeStart, '%Y-%m-%d %H:%M:%S')

        year = str(time_start.year)


        if time_end is not None:

            #timeEnd = datetime.strptime(timeEnd, '%Y-%m-%d %H:%M:%S')

            cql = 'SELECT * FROM ' + table_name + " WHERE output_id=? " \
                                                    "AND field=? " \
                                                    "AND year='"+year+"' " \
                                                    "AND event_time>=? " \
                                                    "AND event_time<=? " \
                                                    "ORDER BY event_time ASC"


            rows = self.execute(cql, [output_id, field_human_name, time_start, time_end])

        else:

            cql = 'SELECT * FROM ' + table_name + " WHERE output_id=? " \
                                        "AND field=? " \
                                        "AND year='"+year+"' " \
                                        "AND event_time>=? " \
                                        "ORDER BY event_time ASC"



            rows = self.execute(cql, [output_id, field_human_name, time_start])

        results = collections.OrderedDict()

        for row in rows:

            results[row.event_time] = row.value

        return results


    def putData(self, output_id, field_human_name, window, value, timestamp):

        year = str(timestamp.year)

        if window == 0:

            table_name = 'output_data_by_field'

        elif window == 1:

            table_name = 'output_data_by_field_minutely'

        elif window == 15:

            table_name = 'output_data_by_field_15_minutely'

        elif window == 60:

            table_name = 'output_data_by_field_hourly'

        else:
            print 'Unknown window requested!!!'



        cql = 'INSERT INTO ' + table_name + ' (output_id, field, year, event_time, value) ' \
                                                                       ' VALUES(?,?,?,?,?)'


        self.execute(cql, [output_id, field_human_name, year, timestamp, str(value)])


    def deleteData(self, output_id, field_human_name, window, timestamp):

        year = str(timestamp.year)

        if window == 0:

            table_name = 'output_data_by_field'

        elif window == 1:

            table_name = 'output_data_by_field_minutely'

        elif window == 15:

            table_name = 'output_data_by_field_15_minutely'

        elif window == 60:

            table_name = 'output_data_by_field_hourly'

        else:
            print 'Unknown window requested!!!'

        cql = 'DELETE FROM ' + table_name + ' WHERE output_id=? and field=? and year=? and event_time=?'

        self.execute(cql, [output_id, field_human_name, year, timestamp])



    def getDateString(self, timestamp):

        month = '%02d' % timestamp.month

        return str(timestamp.year) + '-' + month