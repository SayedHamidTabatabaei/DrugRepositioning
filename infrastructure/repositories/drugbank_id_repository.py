from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class DrugBankIdRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'drugbank_ids'

    def insert(self, drugbank_ids: [], drug_id: int):
        columns = ('drug_id', 'drugbank_id', '`primary`')
        values = [(drug_id, drugbank_id.drugbank_id, drugbank_id.primary) for drugbank_id in drugbank_ids]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)