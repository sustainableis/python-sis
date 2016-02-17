





class Query(object):
    def __init__(self, table_name):

        self._verb = None
        self._from = table_name
        self._fields = []
        self._joins = []
        self._wheres = None
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

    def where(self, where):
        if self._wheres is None:
            self._wheres = Where(where)
        else:
            # TODO -> this is here so we don't break existing code
            # normally we should only call where once and once alone
            self._wheres.AND(where)
        return self

    def AND(self, clause):
        self._wheres.AND(clause)
        return self

    def OR(self, clause):
        self._wheres.OR(clause)
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
            query_chunks.append(str(self._wheres))

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
            query_chunks.append(str(self._wheres))

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
            self._wheres = query._wheres
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
            query_chunks.append(str(self._wheres))

        query_str = ' '.join(query_chunks)

        if self._args is not None:
            query_str = query_str.format(self._args)

        return query_str


class Where(object):
    def __init__(self, first_clause):
        if first_clause is None:
            raise Exception('First clause in WHERE cannot be none')
        self.where = 'WHERE ' + first_clause.strip()

    def AND(self, clause):
        self.where += ' AND ' + clause.strip()
        return self

    def OR(self, clause):
        self.where += ' OR '+clause.strip()
        return self

    def build(self):
        return self.__str__()

    def __str__(self):
        return self.where


def _test_query():
    q = Select('hj_t_location') \
        .fields('field1') \
        .fields('field2') \
        .where('field2 > 3') \
        .where('field1 = 6') \
        .join('hj_t_transaction', [('field1', 'field1'), ('field2', 'field2')]) \
        .order('field1', True) \
        .limit(500)
    count = Count(query=q)
    query_str = str(q)
    count_str = str(count)
    print query_str


def _test_where():
    print(Select("foo").
          fields('bar').
          fields('baz').
          where('f1>f2').
          AND('f2=2').
          OR('f2=5').
          limit(1000))

if __name__ == '__main__':
    _test_query()
    print("\n" + "="*50 + "\n")
    _test_where()


