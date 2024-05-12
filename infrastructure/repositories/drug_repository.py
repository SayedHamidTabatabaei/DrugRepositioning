from common.helpers import mysql_helper
from core.domain.drug import Drug
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class DrugRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "drugs"

    def insert(self, drug: Drug):

        columns = ('name', 'type', 'created_date', 'updated_date', 'description', 'cas_number', 'unii', 'average_mass', 'monoisotopic_mass', 'state',
                   'synthesis_reference', 'indication', 'pharmacodynamics', 'mechanism_of_action', 'toxicity',
                   'metabolism', 'absorption', 'half_life', 'protein_binding', 'route_of_elimination',
                   'volume_of_distribution', 'clearance', 'classification_description', 'classification_direct_parent',
                   'classification_kingdom', 'classification_superclass', 'classification_class_category',
                   'classification_subclass', 'fda_label', 'msds')

        values = (drug.name, drug.type, drug.created, drug.updated, drug.description, drug.cas_number, drug.unii, drug.average_mass, drug.monoisotopic_mass,
                  drug.state, drug.synthesis_reference, drug.indication, drug.pharmacodynamics, drug.mechanism_of_action,
                  drug.toxicity, drug.metabolism, drug.absorption, drug.half_life, drug.protein_binding,
                  drug.route_of_elimination, drug.volume_of_distribution, drug.clearance, drug.classification.description,
                  drug.classification.direct_parent, drug.classification.kingdom, drug.classification.superclass,
                  drug.classification.class_category, drug.classification.subclass, drug.fda_label, drug.msds)

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        return self.execute_query_and_return_last_row_id(insert_query, values)
