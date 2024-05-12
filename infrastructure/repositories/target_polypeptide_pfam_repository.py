from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TargetPolypeptidePfamRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'target_polypeptide_pfams'

    def insert(self, pfams: [], target_polypeptide_id: int):
        columns = ('target_polypeptide_id', 'identifier', 'name')
        values = [(target_polypeptide_id, pfam.identifier, pfam.name) for pfam in pfams]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
