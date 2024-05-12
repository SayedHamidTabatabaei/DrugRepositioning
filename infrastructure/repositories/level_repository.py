from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class LevelRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'levels'

    def insert(self, levels: [], atc_code_id: int):
        columns = ('atc_code_id', 'code', 'value')
        values = [(atc_code_id, level.code, level.value) for level in levels]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
