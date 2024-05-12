from typing import List

from common.helpers import mysql_helper
from core.domain.transporter import Transporter
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TransporterRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'transporters'

    def insert(self, transporters: List[Transporter], drug_id: int) -> List[Transporter]:
        columns = ('drug_id', 'position', 'transporter_id', 'name', 'organism', 'known_action')

        for transporter in transporters:
            values = (drug_id, transporter.position, transporter.id, transporter.name, transporter.organism,
                      transporter.known_action)

            insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
            transporter_id = self.execute_query_and_return_last_row_id(insert_query, values)

            transporter._id = transporter_id

        return transporters
