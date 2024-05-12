from dataclasses import dataclass


@dataclass
class TextBook:
    ref_id: str
    isbn: str
    citation: str
