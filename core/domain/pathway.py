from dataclasses import dataclass


@dataclass
class Pathway:
    smpdb_id: str
    name: str
    category: str
    drugs: []
    enzymes: []
