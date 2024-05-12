from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TargetActionRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'target_actions'

    def insert(self, target_actions: [], target_id: int):
        columns = ('target_id', 'value')
        values = [(target_id, target_action) for target_action in target_actions]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
