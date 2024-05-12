from dataclasses import dataclass


@dataclass
class ExperimentalProperty:
    kind: str
    value: str
    source: str
