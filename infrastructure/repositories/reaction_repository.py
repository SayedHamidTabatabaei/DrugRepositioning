from typing import List

from common.helpers import mysql_helper
from core.domain.reaction import Reaction
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class ReactionRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'reactions'

    def insert(self, reactions: List[Reaction], drug_id: int) -> List[Reaction]:
        columns = ('drug_id', 'sequence')

        for reaction in reactions:
            values = (drug_id, reaction.sequence)

            insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
            reaction_id = self.execute_query_and_return_last_row_id(insert_query, values)

            reaction._id = reaction_id

        return reactions
