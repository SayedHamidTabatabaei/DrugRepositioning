from dataclasses import dataclass


@dataclass
class ReactionEnzyme:
    drugbank_id: str
    name: str
    uniprot_id: str
