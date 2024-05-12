from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class ExperimentalPropertyRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'experimental_properties'

    def insert(self, experimental_properties: [], drug_id: int):
        columns = ('drug_id', 'kind', 'value', 'source')
        values = [(drug_id, experimental_property.kind, experimental_property.value, experimental_property.source) for experimental_property in experimental_properties]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
