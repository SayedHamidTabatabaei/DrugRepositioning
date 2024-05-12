from dataclasses import dataclass


@dataclass
class DrugBankId:
    drugbank_id: str
    primary: bool
