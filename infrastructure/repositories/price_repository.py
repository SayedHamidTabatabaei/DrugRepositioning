from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class PriceRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'prices'

    def insert(self, prices: [], drug_id: int):
        columns = ('drug_id', 'description', 'cost', 'currency', 'unit')
        values = [(drug_id, price.description, price.cost, price.currency, price.unit) for price in prices]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
