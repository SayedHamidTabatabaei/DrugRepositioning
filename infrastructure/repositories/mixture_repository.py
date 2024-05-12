from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class MixtureRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'mixtures'

    def insert(self, mixtures: [], drug_id: int):
        columns = ('drug_id', 'name', 'ingredients')
        values = [(drug_id, mixture.name, mixture.ingredients) for mixture in mixtures]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
