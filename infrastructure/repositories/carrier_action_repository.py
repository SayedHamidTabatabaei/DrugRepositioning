from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class CarrierActionRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'carrier_actions'

    def insert(self, carrier_actions: [], carrier_id: int):
        columns = ('carrier_id', 'value')
        values = [(carrier_id, carrier_action) for carrier_action in carrier_actions]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
