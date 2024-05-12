from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TransporterReferenceArticleRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'transporter_references_articles'

    def insert(self, articles: [], transporter_id: int):
        columns = ('transporter_id', 'ref_id', 'pubmed_id', 'citation')
        values = [(transporter_id, article.ref_id, article.pubmed_id, article.citation) for article in articles]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
