from common.helpers import mysql_helper
from core.domain.element import Element
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class ElementRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'elements'

    def insert(self, element: Element, reaction_id: int, side):
        columns = ('reaction_id', 'drugbank_id', 'name', 'side')

        values = (reaction_id, element.drugbank_id, element.name, side)

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_query_and_return_last_row_id(insert_query, values)
