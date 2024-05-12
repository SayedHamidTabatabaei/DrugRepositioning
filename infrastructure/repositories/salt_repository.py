from typing import List

from common.helpers import mysql_helper
from core.domain.salt import Salt
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class SaltRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'salts'

    def insert(self, salts: List[Salt], drug_id: int) -> List[Salt]:
        columns = ('drug_id', 'name', 'unii', 'cas_number', 'inchikey', 'average_mass', 'monoisotopic_mass')

        for salt in salts:
            values = (drug_id, salt.name, salt.unii, salt.cas_number, salt.inchikey, salt.average_mass, salt.monoisotopic_mass)

            insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
            salt_id = self.execute_many_queries_and_return_last_row_id(insert_query, values)

            salt._id = salt_id

        return salts
