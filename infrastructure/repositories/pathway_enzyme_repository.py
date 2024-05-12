from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class PathwayEnzymeRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'pathway_enzymes'

    def insert(self, enzymes: [], pathway_id: int):
        columns = ('pathway_id', 'uniprot_id')
        values = [(pathway_id, uniprot_id) for uniprot_id in enzymes]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
