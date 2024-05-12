from common.helpers import mysql_helper
from core.domain.polypeptide import Polypeptide
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class EnzymePolypeptideRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'enzyme_polypeptides'

    def insert(self, enzyme_polypeptide: Polypeptide, enzyme_id: int) -> Polypeptide:
        columns = ('enzyme_id', 'polypeptide_id', 'source', 'name', 'general_function', 'specific_function', 'gene_name',
                   'locus', 'cellular_location', 'transmembrane_regions', 'signal_regions', 'theoretical_pi',
                   'molecular_weight', 'chromosome_location', 'organism_ncbi_taxonomy_id', 'organism_ncbi_taxonomy_value',
                   'amino_acid_sequence_format', 'amino_acid_sequence_value', 'gene_sequence_format', 'gene_sequence_value')

        if not hasattr(enzyme_polypeptide, "id"):
            return

        values = (enzyme_id, enzyme_polypeptide.id, enzyme_polypeptide.source, enzyme_polypeptide.name,
                  enzyme_polypeptide.general_function, enzyme_polypeptide.specific_function,
                  enzyme_polypeptide.gene_name, enzyme_polypeptide.locus, enzyme_polypeptide.cellular_location,
                  enzyme_polypeptide.transmembrane_regions, enzyme_polypeptide.signal_regions,
                  enzyme_polypeptide.theoretical_pi, enzyme_polypeptide.molecular_weight,
                  enzyme_polypeptide.chromosome_location, enzyme_polypeptide.organism_ncbi_taxonomy_id,
                  enzyme_polypeptide.organism_ncbi_taxonomy_value, enzyme_polypeptide.amino_acid_sequence_format,
                  enzyme_polypeptide.amino_acid_sequence_value, enzyme_polypeptide.gene_sequence_format,
                  enzyme_polypeptide.gene_sequence_value)

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
        enzyme_polypeptide_id = self.execute_query_and_return_last_row_id(insert_query, values)

        enzyme_polypeptide._id = enzyme_polypeptide_id

        return enzyme_polypeptide
