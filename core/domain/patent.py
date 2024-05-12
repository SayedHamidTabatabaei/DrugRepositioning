from datetime import datetime

from dataclasses import dataclass


@dataclass
class Patent:
    number: str
    country: str
    approved: datetime
    expires: datetime
    pediatric_extension: bool
