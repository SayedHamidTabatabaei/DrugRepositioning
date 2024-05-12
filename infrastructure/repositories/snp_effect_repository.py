from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class SnpEffectRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'snp_effects'

    def insert(self, snp_effects: [], drug_id: int):
        columns = ('drug_id', 'protein_name', 'gene_symbol', 'uniprot_id', 'rs_id', 'allele', 'defining_change',
                   'description', 'pubmed_id')
        values = [(drug_id, snp_effect.protein_name, snp_effect.gene_symbol, snp_effect.uniprot_id, snp_effect.rs_id,
                   snp_effect.allele, snp_effect.defining_change, snp_effect.description, snp_effect.pubmed_id) for snp_effect in snp_effects]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
