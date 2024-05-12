from dataclasses import dataclass


@dataclass
class Link:
    ref_id: str
    title: str
    url: str
