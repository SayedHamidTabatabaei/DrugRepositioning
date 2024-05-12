from dataclasses import dataclass


@dataclass
class Attachment:
    ref_id: str
    title: str
    url: str
