from dataclasses import dataclass


@dataclass
class SnpEffect:
    protein_name: str
    gene_symbol: str
    uniprot_id: str
    rs_id: str
    allele: str
    defining_change: str
    description: str
    pubmed_id: str
