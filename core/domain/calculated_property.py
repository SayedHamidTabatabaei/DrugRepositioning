import decimal

from dataclasses import dataclass


@dataclass
class CalculatedProperty:
    kind: str
    value: decimal
    source: str

