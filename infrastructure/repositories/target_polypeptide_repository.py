from common.helpers import mysql_helper
from core.domain.polypeptide import Polypeptide
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class TargetPolypeptideRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'target_polypeptides'

    def insert(self, target_polypeptide: Polypeptide, target_id: int) -> Polypeptide:
        columns = ('target_id', 'polypeptide_id', 'source', 'name', 'general_function', 'specific_function', 'gene_name',
                   'locus', 'cellular_location', 'transmembrane_regions', 'signal_regions', 'theoretical_pi',
                   'molecular_weight', 'chromosome_location', 'organism_ncbi_taxonomy_id', 'organism_ncbi_taxonomy_value',
                   'amino_acid_sequence_format', 'amino_acid_sequence_value', 'gene_sequence_format', 'gene_sequence_value')

        if not hasattr(target_polypeptide, "id"):
            return

        values = (target_id, target_polypeptide.id, target_polypeptide.source, target_polypeptide.name,
                  target_polypeptide.general_function, target_polypeptide.specific_function,
                  target_polypeptide.gene_name, target_polypeptide.locus, target_polypeptide.cellular_location,
                  target_polypeptide.transmembrane_regions, target_polypeptide.signal_regions,
                  target_polypeptide.theoretical_pi, target_polypeptide.molecular_weight,
                  target_polypeptide.chromosome_location, target_polypeptide.organism_ncbi_taxonomy_id,
                  target_polypeptide.organism_ncbi_taxonomy_value, target_polypeptide.amino_acid_sequence_format,
                  target_polypeptide.amino_acid_sequence_value, target_polypeptide.gene_sequence_format,
                  target_polypeptide.gene_sequence_value)

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
        target_polypeptide_id = self.execute_query_and_return_last_row_id(insert_query, values)

        target_polypeptide._id = target_polypeptide_id

        return target_polypeptide
