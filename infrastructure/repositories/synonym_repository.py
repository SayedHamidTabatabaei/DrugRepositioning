from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class SynonymRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'synonyms'

    def insert(self, synonyms: [], drug_id: int):
        columns = ('drug_id', 'synonym', 'language', 'coder')
        values = [(drug_id, synonym.synonym, synonym.language, synonym.coder) for synonym in synonyms]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
