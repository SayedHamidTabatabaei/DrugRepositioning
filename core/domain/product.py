from dataclasses import dataclass


@dataclass
class Product:
    name: str
    labeller: str
    ndc_id: str
    ndc_product_code: str
    dpd_id: str
    ema_product_code: str
    ema_ma_number: str
    started_marketing_on: str
    ended_marketing_on: str
    dosage_form: str
    strength: str
    route: str
    fda_application_number: str
    generic: bool
    over_the_counter: bool
    approved: bool
    country: str
    source: str
