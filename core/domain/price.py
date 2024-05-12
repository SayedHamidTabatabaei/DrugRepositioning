import decimal

from dataclasses import dataclass


@dataclass
class Price:

    description: str
    cost: decimal
    currency: str
    unit: str