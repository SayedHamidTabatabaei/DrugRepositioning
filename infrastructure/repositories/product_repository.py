from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class ProductRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'products'

    def insert(self, products: [], drug_id: int):
        columns = ('drug_id', 'name', 'labeller', 'ndc_id', 'ndc_product_code', 'dpd_id', 'ema_product_code', 'ema_ma_number', 'started_marketing_on', 'ended_marketing_on',
                   'dosage_form', 'strength', 'route', 'fda_application_number', 'generic', 'over_the_counter', 'approved', 'country', 'source')
        values = [(drug_id, product.name, product.labeller, product.ndc_id, product.ndc_product_code, product.dpd_id, product.ema_product_code, product.ema_ma_number,
                   product.started_marketing_on, product.ended_marketing_on, product.dosage_form, product.strength, product.route, product.fda_application_number,
                   product.generic, product.over_the_counter, product.approved, product.country, product.source) for product in products]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
