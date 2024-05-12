from core.domain.polypeptide import Polypeptide

from dataclasses import dataclass


@dataclass
class Transporter:
    position: int
    id: str
    name: str
    organism: str
    actions: []
    references: []
    known_action: str
    polypeptide: Polypeptide
