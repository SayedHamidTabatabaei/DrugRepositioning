from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class PathwayDrugRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'pathway_drugs'

    def insert(self, pathway_drugs: [], pathway_id: int):
        columns = ('pathway_id', 'drugbank_id', 'name')
        values = [(pathway_id, pathway_drug.drugbank_id, pathway_drug.name) for pathway_drug in pathway_drugs]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
