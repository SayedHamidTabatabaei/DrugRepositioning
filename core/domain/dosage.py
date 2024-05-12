from dataclasses import dataclass


@dataclass
class Dosage:

    form: str
    route: str
    strength: str
