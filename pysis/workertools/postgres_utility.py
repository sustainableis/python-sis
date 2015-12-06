import psycopg2
import psycopg2.extras

class PostgresUtility:

    def __init__(self, host, username, password, database):

        self.connection = psycopg2.connect(dbname=database,
                                           host=host,
                                           user=username,
                                           password=password)


    def execute(self, statement, args=None):

        cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


        if args is not None:

            cursor.execute(statement, args)

        else:

            cursor.execute(statement)


        return cursor.fetchall()







