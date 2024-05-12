import decimal

from dataclasses import dataclass


@dataclass
class Polypeptide:
    id: str
    source: str
    name: str
    general_function: str
    specific_function: str
    gene_name: str
    locus: str
    cellular_location: str
    transmembrane_regions: str
    signal_regions: str
    theoretical_pi: decimal
    molecular_weight: decimal
    chromosome_location: str
    organism_ncbi_taxonomy_id: int | None
    organism_ncbi_taxonomy_value: str
    external_identifiers: []
    synonyms: []
    amino_acid_sequence_format: str
    amino_acid_sequence_value: str
    gene_sequence_format: str
    gene_sequence_value: str
    pfams: []
    go_classifiers: []