from typing import List

from common.helpers import mysql_helper
from core.domain.target import Target
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TargetRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'targets'

    def insert(self, targets: List[Target], drug_id: int) -> List[Target]:
        columns = ('drug_id', 'position', 'target_id', 'name', 'organism', 'known_action')

        for target in targets:
            values = (drug_id, target.position, target.id, target.name, target.organism, target.known_action)

            insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
            target_id = self.execute_query_and_return_last_row_id(insert_query, values)

            target._id = target_id

        return targets
