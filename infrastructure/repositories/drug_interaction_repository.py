from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class DrugInteractionRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'drug_interactions'

    def insert(self, drug_interactions: [], drug_id: int):
        columns = ('drug_id', 'drugbank_id', 'name', 'description')
        values = [(drug_id, drug_interaction.drugbank_id, drug_interaction.name, drug_interaction.description) for drug_interaction in drug_interactions]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
