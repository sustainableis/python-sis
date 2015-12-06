from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from datetime import datetime



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



    def getDateString(self, timestamp):

        month = '%02d' % timestamp.month

        return str(timestamp.year) + '-' + month