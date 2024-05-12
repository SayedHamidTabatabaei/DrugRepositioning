from dataclasses import dataclass


@dataclass
class PathwayDrug:
    drugbank_id: str
    name: str
