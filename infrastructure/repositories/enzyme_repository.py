from typing import List

from common.helpers import mysql_helper
from core.domain.enzyme import Enzyme
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class EnzymeRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'enzymes'

    def insert(self, enzymes: List[Enzyme], drug_id: int) -> List[Enzyme]:
        columns = ('drug_id', 'position', 'enzyme_id', 'name', 'organism', 'known_action', 'inhibition_strength',
                   'induction_strength')

        for enzyme in enzymes:
            values = (drug_id, enzyme.position, enzyme.id, enzyme.name, enzyme.organism, enzyme.known_action,
                      enzyme.inhibition_strength, enzyme.induction_strength)

            insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
            enzyme_id = self.execute_query_and_return_last_row_id(insert_query, values)

            enzyme._id = enzyme_id

        return enzymes
