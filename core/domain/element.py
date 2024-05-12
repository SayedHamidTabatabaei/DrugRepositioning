from dataclasses import dataclass


@dataclass
class Element:
    drugbank_id: str
    name: str
