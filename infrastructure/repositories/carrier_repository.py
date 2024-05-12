from typing import List

from common.helpers import mysql_helper
from core.domain.carrier import Carrier
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class CarrierRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'carriers'

    def insert(self, carriers: List[Carrier], drug_id: int) -> List[Carrier]:
        columns = ('drug_id', 'position', 'carrier_id', 'name', 'organism', 'known_action')

        for carrier in carriers:
            values = (drug_id, carrier.position, carrier.id, carrier.name, carrier.organism, carrier.known_action)

            insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
            carrier_id = self.execute_query_and_return_last_row_id(insert_query, values)

            carrier._id = carrier_id

        return carriers
