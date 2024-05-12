from common.helpers import mysql_helper
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class SnpAdverseDrugReactionRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'snp_adverse_drug_reactions'

    def insert(self, snp_adverse_drug_reactions: [], drug_id: int):
        columns = ('drug_id', 'protein_name', 'gene_symbol', 'uniprot_id', 'rs_id', 'allele', 'adverse_reaction',
                   'description', 'pubmed_id')
        values = [(drug_id, snp_adverse_drug_reaction.protein_name, snp_adverse_drug_reaction.gene_symbol,
                   snp_adverse_drug_reaction.uniprot_id, snp_adverse_drug_reaction.rs_id,
                   snp_adverse_drug_reaction.allele, snp_adverse_drug_reaction.adverse_reaction,
                   snp_adverse_drug_reaction.description, snp_adverse_drug_reaction.pubmed_id) for snp_adverse_drug_reaction in snp_adverse_drug_reactions]

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)

        self.execute_many_queries_and_return_last_row_id(insert_query, values)
