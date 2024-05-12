from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class GeneralReferencesLinkRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'general_references_links'

    def insert(self, links: [], drug_id: int):
        columns = ('drug_id', 'ref_id', 'title', 'url')
        values = [(drug_id, link.ref_id, link.title, link.url) for link in links]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
