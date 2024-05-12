from dataclasses import dataclass


@dataclass
class Article:
    ref_id: str
    pubmed_id: str
    citation: str
