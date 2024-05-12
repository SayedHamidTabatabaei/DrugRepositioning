from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TransporterActionRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'transporter_actions'

    def insert(self, transporter_actions: [], transporter_id: int):
        columns = ('transporter_id', 'value')
        values = [(transporter_id, transporter_action) for transporter_action in transporter_actions]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
