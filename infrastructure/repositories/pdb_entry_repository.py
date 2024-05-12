from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class PdbEntryRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'pdb_entries'

    def insert(self, pdb_entries: [], drug_id: int):
        columns = ('drug_id', 'value')
        values = [(drug_id, pdb_entry) for pdb_entry in pdb_entries]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
