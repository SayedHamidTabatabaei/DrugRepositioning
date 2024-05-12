from common.helpers import mysql_helper
from core.domain.polypeptide import Polypeptide
from infrastructure.mysqldb.mysql_repository import MySqlRepository


class CarrierPolypeptideRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.table_name = 'carrier_polypeptides'

    def insert(self, carrier_polypeptide: Polypeptide, carrier_id: int) -> Polypeptide:
        columns = ('carrier_id', 'polypeptide_id', 'source', 'name', 'general_function', 'specific_function', 'gene_name',
                   'locus', 'cellular_location', 'transmembrane_regions', 'signal_regions', 'theoretical_pi',
                   'molecular_weight', 'chromosome_location', 'organism_ncbi_taxonomy_id', 'organism_ncbi_taxonomy_value',
                   'amino_acid_sequence_format', 'amino_acid_sequence_value', 'gene_sequence_format', 'gene_sequence_value')

        if not hasattr(carrier_polypeptide, "id"):
            return

        values = (carrier_id, carrier_polypeptide.id, carrier_polypeptide.source, carrier_polypeptide.name,
                  carrier_polypeptide.general_function, carrier_polypeptide.specific_function,
                  carrier_polypeptide.gene_name, carrier_polypeptide.locus, carrier_polypeptide.cellular_location,
                  carrier_polypeptide.transmembrane_regions, carrier_polypeptide.signal_regions,
                  carrier_polypeptide.theoretical_pi, carrier_polypeptide.molecular_weight,
                  carrier_polypeptide.chromosome_location, carrier_polypeptide.organism_ncbi_taxonomy_id,
                  carrier_polypeptide.organism_ncbi_taxonomy_value, carrier_polypeptide.amino_acid_sequence_format,
                  carrier_polypeptide.amino_acid_sequence_value, carrier_polypeptide.gene_sequence_format,
                  carrier_polypeptide.gene_sequence_value)

        insert_query = mysql_helper.generate_insert_query(self.table_name, columns)
        carrier_polypeptide_id = self.execute_query_and_return_last_row_id(insert_query, values)

        carrier_polypeptide._id = carrier_polypeptide_id

        return carrier_polypeptide
