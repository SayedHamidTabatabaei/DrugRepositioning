from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class ExternalLinkRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'external_links'

    def insert(self, external_links: [], drug_id: int):
        columns = ('drug_id', 'resource', 'url')
        values = [(drug_id, external_link.resource, external_link.url) for external_link in external_links]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
