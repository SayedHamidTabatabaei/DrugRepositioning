from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class CalculatedPropertyRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'calculated_properties'

    def insert(self, calculated_properties: [], drug_id: int):
        columns = ('drug_id', 'kind', 'value', 'source')
        values = [(drug_id, calculated_property.kind, calculated_property.value, calculated_property.source) for calculated_property in calculated_properties]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)

    def get_calculated_property(self, drug_id, calculated_property):
        pass

    def get_calculated_properties(self, drug_id):
        procedure_name = 'get_drug_calculate_properties'

        return self.call_procedure(procedure_name, drug_id)

    def get_all_drugs_calculated_properties(self):
        procedure_name = 'get_drug_calculate_properties'

        return self.call_procedure(procedure_name, None)

    def get_all_drugs_calculated_property(self, calculated_property):
        pass
