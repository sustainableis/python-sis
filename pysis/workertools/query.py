





class Query(object):
    def __init__(self, table_name):

        self._verb = None
        self._from = table_name
        self._fields = []
        self._joins = []
        self._wheres = []
        self._order = None
        self._limit = None
        self._args = None

    def table(self):

        return self._from

    def verb(self, verb=None):

        if verb is None:
            return self._verb

        else:
            self._verb = verb

            return self

    def fields(self, field=None):

        if field is None:
            return self._fields

        elif type(field) in [list, tuple]:
            self._fields.extend(field)
            return self
        else:
            self._fields.append(field)
            return self

    def where(self, where=None):

        if where is None:
            return self._wheres

        else:
            self._wheres.append(where)

            return self

    def order(self, column=None, desc=None):

        if column is None and desc is None:

            return self._order
        else:
            if desc:
                self._order = 'ORDER BY ' + column + ' DESC'
            else:
                self._order = 'ORDER BY ' + column

            return self

    def join(self, join_table=None, join_conditions=None):

        if join_table is None and join_conditions is None:
            return self._joins

        else:

            # Create condition strings
            conditions = [self._from + '.' + c[0] + ' = ' + join_table + '.' + c[1] for c in join_conditions]

            self._joins.append('JOIN ' + join_table + ' ON ' + ' AND '.join(conditions))

            return self

    def limit(self, limit=None):

        if limit is None:
            return self._limit

        else:
            self._limit = limit

            return self

    def args(self, args=None):

        if args is None:
            return self._args

        else:
            self._args = args

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

        if self._args is not None:
            query_str = query_str.format(self._args)

        return query_str


class Select(Query):

    def __init__(self, table_name):

        super(Select, self).__init__(table_name)

        self._verb = 'SELECT'

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

        if self._order:
            query_chunks.append(self._order)

        if self._limit:

            query_chunks.append('LIMIT ' + str(self._limit))

        query_str = ' '.join(query_chunks)

        if self._args is not None:
            query_str = query_str.format(self._args)

        return query_str


class Count(Select):

    def __init__(self, table_name=None, query=None):

        if table_name:
            super(Count, self).__init__(table_name)

        elif query:
            super(Count, self.__init__(query.table()))

            # copy wheres and joins, but not fields
            self._wheres = query.where()
            self._joins = query.join()

        else:
            raise Exception('table_name or query must be provided!')

    def __str__(self):

        query_chunks = []

        query_chunks.append(self._verb)

        fields_str = ', '.join(self._fields)

        if fields_str:
            query_chunks.append('COUNT(' + fields_str + ')')
        else:
            query_chunks.append('COUNT(1)')

        query_chunks.append('FROM ' + self._from)

        if self._joins:
            query_chunks.append(' '.join(self._joins))

        if self._wheres:
            query_chunks.append('WHERE')
            query_chunks.append(' AND '.join(self._wheres))

        query_str = ' '.join(query_chunks)

        if self._args is not None:
            query_str = query_str.format(self._args)

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

    count = Count(query=q)

    query_str = str(q)

    count_str = str(count)

    print query_str


