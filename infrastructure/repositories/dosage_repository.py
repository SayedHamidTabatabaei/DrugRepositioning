from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class DosageRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'dosages'

    def insert(self, dosages: [], drug_id: int):
        columns = ('drug_id', 'form', 'route', 'strength')
        values = [(drug_id, dosage.form, dosage.route, dosage.strength) for dosage in dosages]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
