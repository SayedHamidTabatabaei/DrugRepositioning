from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class SubstituentRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'substituents'

    def insert(self, substituents: [], drug_id: int):
        columns = ('drug_id', 'value')
        values = [(drug_id, substituent) for substituent in substituents]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
