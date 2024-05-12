from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class SaltDrugbankIdRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'salt_drugbank_ids'

    def insert(self, salt_drugbank_ids: [], salt_id: int):
        columns = ('salt_id', 'drugbank_id', '`primary`')
        values = [(salt_id, salt_drugbank_id.drugbank_id, salt_drugbank_id.primary) for salt_drugbank_id in salt_drugbank_ids]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
