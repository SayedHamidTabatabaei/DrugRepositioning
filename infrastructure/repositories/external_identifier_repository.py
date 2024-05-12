from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class ExternalIdentifierRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'external_identifiers'

    def insert(self, external_identifiers: [], drug_id: int):
        columns = ('drug_id', 'resource', 'identifier')
        values = [(drug_id, external_identifier.resource, external_identifier.identifier) for external_identifier in external_identifiers]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
