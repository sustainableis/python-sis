





class Query(object):

    def __init__(self, table_name):

        self._verb = None
        self._from = table_name
        self._fields = []
        self._joins = []
        self._wheres = []
        self._order = None
        self._limit = None

    def verb(self, verb):

        self._verb = verb

        return self

    def fields(self, columns):

        self._fields.append(columns)

        return self

    def where(self, where_clause):

        self._wheres.append(where_clause)

        return self

    def order(self, key, desc=None):

        if desc:
            self._order = 'ORDER BY ' + key + ' DESC'
        else:
            self._order = 'ORDER BY ' + key

        return self

    def join(self, table, conditions):

        # Create condition strings
        conditions = [self._from + '.' + c[0] + ' = ' + table + '.' + c[1] for c in conditions]

        self._joins.append('JOIN ' + table + ' ON ' + ' AND '.join(conditions))

        return self

    def limit(self, limit):

        self._limit = limit

        return self

    def __str__(self):

        query_chunks = []

        query_chunks.append(self._verb)

        query_chunks.append(', '.join(self._fields))

        query_chunks.append('FROM ' + self._from)

        if self._joins:
            query_chunks.append(' '.join(self._joins))

        if self._wheres:
            query_chunks.append('WHERE')
            query_chunks.append(' AND '.join(self._wheres))

        if self._limit:

            query_chunks.append('LIMIT ' + str(self._limit))

        if self._order:
            query_chunks.append(self._order)

        query_str = ' '.join(query_chunks)

        return query_str


class Select(Query):

    def __init__(self, table_name):

        super(Select, self).__init__(table_name)

        self._verb = 'SELECT'

        self._count = False

    def count(self):

        self._count = True

    def __str__(self):

        query_chunks = []

        query_chunks.append(self._verb)

        fields_str = ', '.join(self._fields)

        if self._count:

            if fields_str:

                query_chunks.append('COUNT('+fields_str+')')

            else:
                query_chunks.append('COUNT(1)')

        else:
            query_chunks.append(fields_str)

        query_chunks.append('FROM ' + self._from)

        if self._joins:
            query_chunks.append(' '.join(self._joins))

        if self._wheres:
            query_chunks.append('WHERE')
            query_chunks.append(' AND '.join(self._wheres))

        if self._order:
            query_chunks.append(self._order)

        if self._limit:

            query_chunks.append('LIMIT ' + str(self._limit))

        query_str = ' '.join(query_chunks)

        return query_str


if __name__ == '__main__':

    q = Select('hj_t_location')\
        .fields('field1')\
        .fields('field2')\
        .where('field2 > 3')\
        .where('field1 = 6')\
        .join('hj_t_transaction', [('field1', 'field1'), ('field2', 'field2')])\
        .order('field1', True)\
        .limit(500)

    query_str = str(q)

    print query_str


