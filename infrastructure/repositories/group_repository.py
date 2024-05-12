from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class GroupRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = '`groups`'

    def insert(self, groups: [], drug_id: int):
        columns = ('drug_id', 'value')
        values = [(drug_id, group) for group in groups]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
