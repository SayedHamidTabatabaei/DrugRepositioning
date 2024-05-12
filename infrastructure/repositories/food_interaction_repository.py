from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class FoodInteractionRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'food_interactions'

    def insert(self, food_interactions: [], drug_id: int):
        columns = ('drug_id', 'value')
        values = [(drug_id, food_interaction) for food_interaction in food_interactions]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
