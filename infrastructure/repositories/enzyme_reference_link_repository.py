from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class EnzymeReferenceLinkRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'enzyme_references_links'

    def insert(self, links: [], enzyme_id: int):
        columns = ('enzyme_id', 'ref_id', 'title', 'url')
        values = [(enzyme_id, link.ref_id, link.title, link.url) for link in links]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
