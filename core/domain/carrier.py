from core.domain.polypeptide import Polypeptide

from dataclasses import dataclass


@dataclass
class Carrier:
    position: int
    id: str
    name: str
    organism: str
    actions: []
    references: []
    known_action: str
    polypeptide: Polypeptide
