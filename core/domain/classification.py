from dataclasses import dataclass


@dataclass(init=False)
class Classification:
    description: str
    direct_parent: str
    kingdom: str
    superclass: str
    class_category: str
    subclass: str
    alternative_parent: []
    substituent: []

    def __init__(self):
        self.description = ""
        self.direct_parent = ""
        self.kingdom = ""
        self.superclass = ""
        self.class_category = ""
        self.subclass = ""
        self.alternative_parent = []
        self.substituent = []
