import decimal

from dataclasses import dataclass


@dataclass
class Salt:
    drugbank_id: []
    name: str
    unii: str
    cas_number: str
    inchikey: str
    average_mass: decimal
    monoisotopic_mass: decimal
