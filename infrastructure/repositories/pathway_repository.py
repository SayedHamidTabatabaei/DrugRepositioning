from typing import List

from common.helpers import mysql_helper
from core.domain.pathway import Pathway
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class PathwayRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'pathways'

    def insert(self, pathways: List[Pathway], drug_id: int) -> List[Pathway]:
        columns = ('drug_id', 'smpdb_id', 'name', 'category')

        for pathway in pathways:
            values = (drug_id, pathway.smpdb_id, pathway.name, pathway.category)

            insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
            pathway_id = self.execute_query_and_return_last_row_id(insert_query, values)

            pathway._id = pathway_id

        return pathways
