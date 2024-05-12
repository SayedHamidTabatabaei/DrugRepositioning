from dataclasses import dataclass


@dataclass
class ExternalLink:
    resource: str
    url: str
