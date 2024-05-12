from dataclasses import dataclass


@dataclass
class DrugInteraction:
    drugbank_id: str
    name: str
    description: str
