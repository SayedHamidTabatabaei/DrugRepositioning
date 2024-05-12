from dataclasses import dataclass


@dataclass
class Synonym:
    synonym: str
    language: str
    coder: str
