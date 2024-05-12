import decimal
from dataclasses import dataclass
from datetime import datetime

from core.domain.classification import Classification
from core.domain.general_references import GeneralReferences


@dataclass(init=False)
class Drug:
    type: str
    created: datetime
    updated: datetime
    drugbank_ids: []
    name: str
    description: str
    cas_number: str
    unii: str
    average_mass: decimal
    monoisotopic_mass: decimal
    state: str
    groups: []
    general_references: GeneralReferences
    synthesis_reference: str
    indication: str
    pharmacodynamics: str
    mechanism_of_action: str
    toxicity: str
    metabolism: str
    absorption: str
    half_life: str
    protein_binding: str
    route_of_elimination: str
    volume_of_distribution: str
    clearance: str
    classification: Classification
    salts: []
    synonyms: []
    products: []
    international_brands: []
    mixtures: []
    packagers: []
    manufacturers: []
    prices: []
    categories: []
    affected_organisms: []
    dosages: []
    atc_codes: []
    pdb_entries: []
    fda_label: str
    msds: str
    patents: []
    food_interactions: []
    drug_interactions: []
    calculated_properties: []
    sequences: []
    experimental_properties: []
    external_identifiers: []
    external_links: []
    pathways: []
    reactions: []
    snp_effects: []
    snp_adverse_drug_reactions: []
    targets: []
    enzymes: []
    carriers: []
    transporters: []

    def __init__(self):
        self.typd = ""
        self.created = datetime.utcnow()
        self.updated = datetime.utcnow()
        self.drugbank_ids = []
        self.name = ""
        self.description = ""
        self.cas_number = ""
        self.unii = ""
        self.average_mass = 0.0
        self.monoisotopic_mass = 0.0
        self.state = ""
        self.groups = []
        self.general_references = GeneralReferences()
        self.synthesis_reference = ""
        self.indication = ""
        self.pharmacodynamics = ""
        self.mechanism_of_action = ""
        self.toxicity = ""
        self.metabolism = ""
        self.absorption = ""
        self.half_life = ""
        self.protein_binding = ""
        self.route_of_elimination = ""
        self.volume_of_distribution = ""
        self.clearance = ""
        self.classification = Classification()
        self.salts = []
        self.synonyms = []
        self.products = []
        self.international_brands = []
        self.mixtures = []
        self.packagers = []
        self.manufacturers = []
        self.prices = []
        self.categories = []
        self.affected_organisms = []
        self.dosages = []
        self.atc_codes = []
        self.pdb_entries = []
        self.fda_label = ''
        self.msds = ''
        self.patents = []
        self.food_interactions = []
        self.drug_interactions = []
        self.calculated_properties = []
        self.sequences = []
        self.experimental_properties = []
        self.external_identifiers = []
        self.external_links = []
        self.pathways = []
        self.reactions = []
        self.snp_effects = []
        self.snp_adverse_drug_reactions = []
        self.targets = []
        self.enzymes = []
        self.carriers = []
        self.transporters = []


