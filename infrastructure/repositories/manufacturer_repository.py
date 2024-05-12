from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class ManufacturerRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'manufacturers'

    def insert(self, manufacturers: [], drug_id: int):
        columns = ('drug_id', 'value', 'generic', 'url')
        values = [(drug_id, manufacturer.value, manufacturer.generic, manufacturer.url) for manufacturer in manufacturers]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
