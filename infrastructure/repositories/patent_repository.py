from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class PatentRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'patents'

    def insert(self, patents: [], drug_id: int):
        columns = ('drug_id', 'number', 'country', 'approved', 'expires', 'pediatric_extension')
        values = [(drug_id, patent.number, patent.country, patent.approved, patent.expires, patent.pediatric_extension) for patent in patents]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
