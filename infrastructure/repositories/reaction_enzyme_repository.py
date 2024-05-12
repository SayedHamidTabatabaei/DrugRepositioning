from typing import List

from common.helpers import mysql_helper
from core.domain.enzyme import Enzyme
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class ReactionEnzymeRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'reaction_enzymes'

    def insert(self, enzymes: List[Enzyme], reaction_id: int):
        columns = ('reaction_id', 'drugbank_id', 'name', 'uniprot_id')
        values = [(reaction_id, enzyme.drugbank_id, enzyme.name, enzyme.uniprot_id) for enzyme in enzymes]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
