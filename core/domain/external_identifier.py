from dataclasses import dataclass


@dataclass
class ExternalIdentifier:
    resource: str
    identifier: str
