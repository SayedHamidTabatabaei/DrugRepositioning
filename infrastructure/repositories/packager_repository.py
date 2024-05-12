from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class PackagerRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'packagers'

    def insert(self, packagers: [], drug_id: int):
        columns = ('drug_id', 'name', 'url')
        values = [(drug_id, packager.name, packager.url) for packager in packagers]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
