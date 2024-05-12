from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class InternationalBrandRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'international_brands'

    def insert(self, international_brands: [], drug_id: int):
        columns = ('drug_id', 'name', 'company')
        values = [(drug_id, international_brand.name, international_brand.company) for international_brand in international_brands]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
