from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class EnzymeActionRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'enzyme_actions'

    def insert(self, enzyme_actions: [], enzyme_id: int):
        columns = ('enzyme_id', 'value')
        values = [(enzyme_id, enzyme_action) for enzyme_action in enzyme_actions]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
