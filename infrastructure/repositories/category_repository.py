from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class CategoryRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'categories'

    def insert(self, categories: [], drug_id: int):
        columns = ('drug_id', 'category', 'mesh_id')
        values = [(drug_id, category.category, category.mesh_id) for category in categories]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
