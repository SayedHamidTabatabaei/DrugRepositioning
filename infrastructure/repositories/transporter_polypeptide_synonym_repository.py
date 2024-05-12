from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TransporterPolypeptideSynonymRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'transporter_polypeptide_synonyms'

    def insert(self, synonyms: [], transporter_polypeptide_id: int):
        columns = ('transporter_polypeptide_id', 'synonym', 'language', 'coder')
        values = [(transporter_polypeptide_id, synonym.synonym, synonym.language, synonym.coder) for synonym in synonyms]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
