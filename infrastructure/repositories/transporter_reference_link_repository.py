from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TransporterReferenceLinkRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'transporter_references_links'

    def insert(self, links: [], transporter_id: int):
        columns = ('transporter_id', 'ref_id', 'title', 'url')
        values = [(transporter_id, link.ref_id, link.title, link.url) for link in links]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
