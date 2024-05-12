from dataclasses import dataclass


@dataclass
class SnpAdverseDrugReaction:
    protein_name: str
    gene_symbol: str
    uniprot_id: str
    rs_id: str
    allele: str
    adverse_reaction: str
    description: str
    pubmed_id: str
