from typing import List

from common.helpers import mysql_helper
from core.domain.atc_code import AtcCode
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class AtcCodeRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'atc_codes'

    def insert(self, atc_codes: List[AtcCode], drug_id: int) -> List[AtcCode]:
        columns = ('drug_id', 'code')

        for atc_code in atc_codes:
            values = (drug_id, atc_code.code)
            insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

            atc_code_id = self.execute_query_and_return_last_row_id(insert_query, values)

            atc_code._id = atc_code_id

        return atc_codes
