from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TargetReferenceTextbookRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'target_references_textbooks'

    def insert(self, textbooks: [], target_id: int):
        columns = ('target_id', 'ref_id', 'isbn', 'citation')
        values = [(target_id, textbook.ref_id, textbook.isbn, textbook.citation) for textbook in textbooks]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)