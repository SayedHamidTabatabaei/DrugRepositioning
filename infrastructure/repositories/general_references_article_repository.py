from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class GeneralReferencesArticleRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'general_references_articles'

    def insert(self, articles: [], drug_id: int):
        columns = ('drug_id', 'ref_id', 'citation')
        values = [(drug_id, article.ref_id, article.citation) for article in articles]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
