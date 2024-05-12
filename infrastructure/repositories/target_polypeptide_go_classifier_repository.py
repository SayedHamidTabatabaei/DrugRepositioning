from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TargetPolypeptideGoClassifierRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'target_polypeptide_go_classifiers'

    def insert(self, go_classifiers: [], target_polypeptide_id: int):
        columns = ('target_polypeptide_id', 'category', 'description')
        values = [(target_polypeptide_id, go_classifier.category, go_classifier.description) for go_classifier in go_classifiers]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
