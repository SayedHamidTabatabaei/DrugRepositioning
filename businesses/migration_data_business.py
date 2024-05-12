from datetime import datetime
from xml.dom import minidom

from core.domain.drug import Drug
from core.mapper.drug_mapper import map_drug
from infrastructure.mysqldb import mysql_repository
from infrastructure.repositories import drug_repository
from infrastructure.repositories import drugbank_id_repository
from infrastructure.repositories import generate_database_repository
from infrastructure.repositories import group_repository
from infrastructure.repositories import general_references_article_repository
from infrastructure.repositories import general_references_attachment_repository
from infrastructure.repositories import general_references_link_repository
from infrastructure.repositories import general_references_textbook_repository
from infrastructure.repositories import alternative_parent_repository
from infrastructure.repositories import substituent_repository
from infrastructure.repositories import salt_repository
from infrastructure.repositories import salt_drugbank_id_repository
from infrastructure.repositories import synonym_repository
from infrastructure.repositories import product_repository
from infrastructure.repositories import international_brand_repository
from infrastructure.repositories import mixture_repository
from infrastructure.repositories import packager_repository
from infrastructure.repositories import manufacturer_repository
from infrastructure.repositories import price_repository
from infrastructure.repositories import category_repository
from infrastructure.repositories import affected_organism_repository
from infrastructure.repositories import dosage_repository
from infrastructure.repositories import atc_code_repository
from infrastructure.repositories import level_repository
from infrastructure.repositories import pdb_entry_repository
from infrastructure.repositories import patent_repository
from infrastructure.repositories import food_interaction_repository
from infrastructure.repositories import drug_interaction_repository
from infrastructure.repositories import calculated_property_repository
from infrastructure.repositories import sequence_repository
from infrastructure.repositories import experimental_property_repository
from infrastructure.repositories import external_identifier_repository
from infrastructure.repositories import external_link_repository
from infrastructure.repositories import pathway_repository
from infrastructure.repositories import pathway_enzyme_repository
from infrastructure.repositories import pathway_drug_repository
from infrastructure.repositories import element_repository
from infrastructure.repositories import reaction_enzyme_repository
from infrastructure.repositories import reaction_repository
from infrastructure.repositories import snp_effect_repository
from infrastructure.repositories import snp_adverse_drug_reaction_repository
from infrastructure.repositories import target_action_repository
from infrastructure.repositories import target_polypeptide_external_identifier_repository
from infrastructure.repositories import target_polypeptide_go_classifier_repository
from infrastructure.repositories import target_polypeptide_pfam_repository
from infrastructure.repositories import target_polypeptide_synonym_repository
from infrastructure.repositories import target_polypeptide_repository
from infrastructure.repositories import target_reference_article_repository
from infrastructure.repositories import target_reference_attachment_repository
from infrastructure.repositories import target_reference_link_repository
from infrastructure.repositories import target_reference_textbook_repository
from infrastructure.repositories import target_repository
from infrastructure.repositories import enzyme_action_repository
from infrastructure.repositories import enzyme_polypeptide_external_identifier_repository
from infrastructure.repositories import enzyme_polypeptide_go_classifier_repository
from infrastructure.repositories import enzyme_polypeptide_pfam_repository
from infrastructure.repositories import enzyme_polypeptide_synonym_repository
from infrastructure.repositories import enzyme_polypeptide_repository
from infrastructure.repositories import enzyme_reference_article_repository
from infrastructure.repositories import enzyme_reference_attachment_repository
from infrastructure.repositories import enzyme_reference_link_repository
from infrastructure.repositories import enzyme_reference_textbook_repository
from infrastructure.repositories import enzyme_repository
from infrastructure.repositories import carrier_action_repository
from infrastructure.repositories import carrier_polypeptide_external_identifier_repository
from infrastructure.repositories import carrier_polypeptide_go_classifier_repository
from infrastructure.repositories import carrier_polypeptide_pfam_repository
from infrastructure.repositories import carrier_polypeptide_synonym_repository
from infrastructure.repositories import carrier_polypeptide_repository
from infrastructure.repositories import carrier_reference_article_repository
from infrastructure.repositories import carrier_reference_attachment_repository
from infrastructure.repositories import carrier_reference_link_repository
from infrastructure.repositories import carrier_reference_textbook_repository
from infrastructure.repositories import carrier_repository
from infrastructure.repositories import transporter_action_repository
from infrastructure.repositories import transporter_polypeptide_external_identifier_repository
from infrastructure.repositories import transporter_polypeptide_go_classifier_repository
from infrastructure.repositories import transporter_polypeptide_pfam_repository
from infrastructure.repositories import transporter_polypeptide_synonym_repository
from infrastructure.repositories import transporter_polypeptide_repository
from infrastructure.repositories import transporter_reference_article_repository
from infrastructure.repositories import transporter_reference_attachment_repository
from infrastructure.repositories import transporter_reference_link_repository
from infrastructure.repositories import transporter_reference_textbook_repository
from infrastructure.repositories import transporter_repository


class MigrationDataBusiness(object):
    def __init__(self):
        self.mysql_repository = mysql_repository.MySqlRepository()
        self.generate_database_repository = generate_database_repository.GenerateDatabaseRepository()
        self.drug_repository = drug_repository.DrugRepository()
        self.drugbank_id_repository = drugbank_id_repository.DrugBankIdRepository()
        self.group_repository = group_repository.GroupRepository()
        self.general_references_article_repository = general_references_article_repository.GeneralReferencesArticleRepository()
        self.general_references_attachment_repository = general_references_attachment_repository.GeneralReferencesAttachmentRepository()
        self.general_references_link_repository = general_references_link_repository.GeneralReferencesLinkRepository()
        self.general_references_textbook_repository = general_references_textbook_repository.GeneralReferencesTextbookRepository()
        self.alternative_parent_repository = alternative_parent_repository.AlternativeParentRepository()
        self.substituent_repository = substituent_repository.SubstituentRepository()
        self.salt_repository = salt_repository.SaltRepository()
        self.salt_drugbank_id_repository = salt_drugbank_id_repository.SaltDrugbankIdRepository()
        self.synonym_repository = synonym_repository.SynonymRepository()
        self.product_repository = product_repository.ProductRepository()
        self.international_brand_repository = international_brand_repository.InternationalBrandRepository()
        self.mixture_repository = mixture_repository.MixtureRepository()
        self.packager_repository = packager_repository.PackagerRepository()
        self.manufacturer_repository = manufacturer_repository.ManufacturerRepository()
        self.price_repository = price_repository.PriceRepository()
        self.category_repository = category_repository.CategoryRepository()
        self.affected_organism_repository = affected_organism_repository.AffectedOrganismRepository()
        self.dosage_repository = dosage_repository.DosageRepository()
        self.atc_code_repository = atc_code_repository.AtcCodeRepository()
        self.level_repository = level_repository.LevelRepository()
        self.pdb_entry_repository = pdb_entry_repository.PdbEntryRepository()
        self.patent_repository = patent_repository.PatentRepository()
        self.food_interaction_repository = food_interaction_repository.FoodInteractionRepository()
        self.drug_interaction_repository = drug_interaction_repository.DrugInteractionRepository()
        self.calculated_property_repository = calculated_property_repository.CalculatedPropertyRepository()
        self.sequence_repository = sequence_repository.SequenceRepository()
        self.experimental_property_repository = experimental_property_repository.ExperimentalPropertyRepository()
        self.external_identifier_repository = external_identifier_repository.ExternalIdentifierRepository()
        self.external_link_repository = external_link_repository.ExternalLinkRepository()
        self.pathway_repository = pathway_repository.PathwayRepository()
        self.pathway_enzyme_repository = pathway_enzyme_repository.PathwayEnzymeRepository()
        self.pathway_drug_repository = pathway_drug_repository.PathwayDrugRepository()
        self.element_repository = element_repository.ElementRepository()
        self.reaction_enzyme_repository = reaction_enzyme_repository.ReactionEnzymeRepository()
        self.reaction_repository = reaction_repository.ReactionRepository()
        self.snp_effect_repository = snp_effect_repository.SnpEffectRepository()
        self.snp_adverse_drug_reaction_repository = snp_adverse_drug_reaction_repository.SnpAdverseDrugReactionRepository()
        self.target_action_repository = target_action_repository.TargetActionRepository()
        self.target_polypeptide_external_identifier_repository = target_polypeptide_external_identifier_repository.TargetPolypeptideExternalIdentifierRepository()
        self.target_polypeptide_go_classifier_repository = target_polypeptide_go_classifier_repository.TargetPolypeptideGoClassifierRepository()
        self.target_polypeptide_pfam_repository = target_polypeptide_pfam_repository.TargetPolypeptidePfamRepository()
        self.target_polypeptide_synonym_repository = target_polypeptide_synonym_repository.TargetPolypeptideSynonymRepository()
        self.target_polypeptide_repository = target_polypeptide_repository.TargetPolypeptideRepository()
        self.target_reference_article_repository = target_reference_article_repository.TargetReferenceArticleRepository()
        self.target_reference_attachment_repository = target_reference_attachment_repository.TargetReferenceAttachmentRepository()
        self.target_reference_link_repository = target_reference_link_repository.TargetReferenceLinkRepository()
        self.target_reference_textbook_repository = target_reference_textbook_repository.TargetReferenceTextbookRepository()
        self.target_repository = target_repository.TargetRepository()
        self.enzyme_action_repository = enzyme_action_repository.EnzymeActionRepository()
        self.enzyme_polypeptide_external_identifier_repository = enzyme_polypeptide_external_identifier_repository.EnzymePolypeptideExternalIdentifierRepository()
        self.enzyme_polypeptide_go_classifier_repository = enzyme_polypeptide_go_classifier_repository.EnzymePolypeptideGoClassifierRepository()
        self.enzyme_polypeptide_pfam_repository = enzyme_polypeptide_pfam_repository.EnzymePolypeptidePfamRepository()
        self.enzyme_polypeptide_synonym_repository = enzyme_polypeptide_synonym_repository.EnzymePolypeptideSynonymRepository()
        self.enzyme_polypeptide_repository = enzyme_polypeptide_repository.EnzymePolypeptideRepository()
        self.enzyme_reference_article_repository = enzyme_reference_article_repository.EnzymeReferenceArticleRepository()
        self.enzyme_reference_attachment_repository = enzyme_reference_attachment_repository.EnzymeReferenceAttachmentRepository()
        self.enzyme_reference_link_repository = enzyme_reference_link_repository.EnzymeReferenceLinkRepository()
        self.enzyme_reference_textbook_repository = enzyme_reference_textbook_repository.EnzymeReferenceTextbookRepository()
        self.enzyme_repository = enzyme_repository.EnzymeRepository()
        self.carrier_action_repository = carrier_action_repository.CarrierActionRepository()
        self.carrier_polypeptide_external_identifier_repository = carrier_polypeptide_external_identifier_repository.CarrierPolypeptideExternalIdentifierRepository()
        self.carrier_polypeptide_go_classifier_repository = carrier_polypeptide_go_classifier_repository.CarrierPolypeptideGoClassifierRepository()
        self.carrier_polypeptide_pfam_repository = carrier_polypeptide_pfam_repository.CarrierPolypeptidePfamRepository()
        self.carrier_polypeptide_synonym_repository = carrier_polypeptide_synonym_repository.CarrierPolypeptideSynonymRepository()
        self.carrier_polypeptide_repository = carrier_polypeptide_repository.CarrierPolypeptideRepository()
        self.carrier_reference_article_repository = carrier_reference_article_repository.CarrierReferenceArticleRepository()
        self.carrier_reference_attachment_repository = carrier_reference_attachment_repository.CarrierReferenceAttachmentRepository()
        self.carrier_reference_link_repository = carrier_reference_link_repository.CarrierReferenceLinkRepository()
        self.carrier_reference_textbook_repository = carrier_reference_textbook_repository.CarrierReferenceTextbookRepository()
        self.carrier_repository = carrier_repository.CarrierRepository()
        self.transporter_action_repository = transporter_action_repository.TransporterActionRepository()
        self.transporter_polypeptide_external_identifier_repository = transporter_polypeptide_external_identifier_repository.TransporterPolypeptideExternalIdentifierRepository()
        self.transporter_polypeptide_go_classifier_repository = transporter_polypeptide_go_classifier_repository.TransporterPolypeptideGoClassifierRepository()
        self.transporter_polypeptide_pfam_repository = transporter_polypeptide_pfam_repository.TransporterPolypeptidePfamRepository()
        self.transporter_polypeptide_synonym_repository = transporter_polypeptide_synonym_repository.TransporterPolypeptideSynonymRepository()
        self.transporter_polypeptide_repository = transporter_polypeptide_repository.TransporterPolypeptideRepository()
        self.transporter_reference_article_repository = transporter_reference_article_repository.TransporterReferenceArticleRepository()
        self.transporter_reference_attachment_repository = transporter_reference_attachment_repository.TransporterReferenceAttachmentRepository()
        self.transporter_reference_link_repository = transporter_reference_link_repository.TransporterReferenceLinkRepository()
        self.transporter_reference_textbook_repository = transporter_reference_textbook_repository.TransporterReferenceTextbookRepository()
        self.transporter_repository = transporter_repository.TransporterRepository()

    def start(self, file_name: str):
        if not file_name:
            raise Exception("file_name cannot be empty")

        print('start to read file ' + file_name + ' at ' + str(datetime.now()))

        file = minidom.parse(file_name)

        print('file uploaded at ' + str(datetime.now()))

        self.migrate(file)

        print('finished at ' + str(datetime.now()))

    def migrate(self, file):
        print('generate database started!')
        self.generate_database_repository.generate_database()
        print('generate database finished!')

        i = 1

        for item in file.childNodes[0].childNodes:

            if item.nodeName == "#text" and item.nodeValue == '\n':
                continue

            drug = map_drug(item)

            print(f'Start insert file {str(i)}')
            i += 1

            self.insert_into_drugs(drug)

    def insert_into_drugs(self, drug: Drug):
        drug_id = self.drug_repository.insert(drug)

        self.drugbank_id_repository.insert(drug.drugbank_ids, drug_id)

        self.group_repository.insert(drug.groups, drug_id)

        self.general_references_article_repository.insert(drug.general_references.articles, drug_id)

        self.general_references_attachment_repository.insert(drug.general_references.attachments, drug_id)

        self.general_references_link_repository.insert(drug.general_references.links, drug_id)

        self.general_references_textbook_repository.insert(drug.general_references.textbooks, drug_id)

        self.alternative_parent_repository.insert(drug.classification.alternative_parent, drug_id)

        self.substituent_repository.insert(drug.classification.substituent, drug_id)

        salts = self.salt_repository.insert(drug.salts, drug_id)

        for salt in salts:
            self.salt_drugbank_id_repository.insert(salt.drugbank_id, salt._id)

        self.synonym_repository.insert(drug.synonyms, drug_id)

        self.product_repository.insert(drug.products, drug_id)

        self.international_brand_repository.insert(drug.international_brands, drug_id)

        self.mixture_repository.insert(drug.mixtures, drug_id)

        self.packager_repository.insert(drug.packagers, drug_id)

        self.manufacturer_repository.insert(drug.manufacturers, drug_id)

        self.price_repository.insert(drug.prices, drug_id)

        self.category_repository.insert(drug.categories, drug_id)

        self.affected_organism_repository.insert(drug.affected_organisms, drug_id)

        self.dosage_repository.insert(drug.dosages, drug_id)

        atc_codes = self.atc_code_repository.insert(drug.atc_codes, drug_id)

        for atc_code in atc_codes:
            self.level_repository.insert(atc_code.levels, atc_code._id)

        self.pdb_entry_repository.insert(drug.pdb_entries, drug_id)

        self.patent_repository.insert(drug.patents, drug_id)

        self.food_interaction_repository.insert(drug.food_interactions, drug_id)

        self.drug_interaction_repository.insert(drug.drug_interactions, drug_id)

        self.calculated_property_repository.insert(drug.calculated_properties, drug_id)

        self.sequence_repository.insert(drug.sequences, drug_id)

        self.experimental_property_repository.insert(drug.experimental_properties, drug_id)

        self.external_identifier_repository.insert(drug.external_identifiers, drug_id)

        self.external_link_repository.insert(drug.external_links, drug_id)

        pathways = self.pathway_repository.insert(drug.pathways, drug_id)

        for pathway in pathways:
            self.pathway_enzyme_repository.insert(pathway.enzymes, pathway._id)
            self.pathway_drug_repository.insert(pathway.drugs, pathway._id)

        reactions = self.reaction_repository.insert(drug.reactions, drug_id)

        for reaction in reactions:
            self.element_repository.insert(reaction.left_element, reaction._id, 'left')
            self.element_repository.insert(reaction.right_element, reaction._id, 'right')
            self.reaction_enzyme_repository.insert(reaction.enzymes, reaction._id)

        self.snp_effect_repository.insert(drug.snp_effects, drug_id)

        self.snp_adverse_drug_reaction_repository.insert(drug.snp_adverse_drug_reactions, drug_id)

        targets = self.target_repository.insert(drug.targets, drug_id)

        for target in targets:
            self.target_action_repository.insert(target.actions, target._id)

            target_polypeptide = self.target_polypeptide_repository.insert(target.polypeptide, target._id)
            self.target_polypeptide_external_identifier_repository.insert(target_polypeptide.external_identifiers, target_polypeptide._id)
            self.target_polypeptide_go_classifier_repository.insert(target_polypeptide.go_classifiers, target_polypeptide._id)
            self.target_polypeptide_pfam_repository.insert(target_polypeptide.pfams, target_polypeptide._id)
            self.target_polypeptide_synonym_repository.insert(target_polypeptide.synonyms, target_polypeptide._id)

            self.target_reference_article_repository.insert(target.references.articles, target._id)
            self.target_reference_attachment_repository.insert(target.references.attachments, target._id)
            self.target_reference_link_repository.insert(target.references.links, target._id)
            self.target_reference_textbook_repository.insert(target.references.textbooks, target._id)

        enzymes = self.enzyme_repository.insert(drug.enzymes, drug_id)

        for enzyme in enzymes:
            self.enzyme_action_repository.insert(enzyme.actions, enzyme._id)

            enzyme_polypeptide = self.enzyme_polypeptide_repository.insert(enzyme.polypeptide, enzyme._id)
            self.enzyme_polypeptide_external_identifier_repository.insert(enzyme_polypeptide.external_identifiers, enzyme_polypeptide._id)
            self.enzyme_polypeptide_go_classifier_repository.insert(enzyme_polypeptide.go_classifiers, enzyme_polypeptide._id)
            self.enzyme_polypeptide_pfam_repository.insert(enzyme_polypeptide.pfams, enzyme_polypeptide._id)
            self.enzyme_polypeptide_synonym_repository.insert(enzyme_polypeptide.synonyms, enzyme_polypeptide._id)

            self.enzyme_reference_article_repository.insert(enzyme.references.articles, enzyme._id)
            self.enzyme_reference_attachment_repository.insert(enzyme.references.attachments, enzyme._id)
            self.enzyme_reference_link_repository.insert(enzyme.references.links, enzyme._id)
            self.enzyme_reference_textbook_repository.insert(enzyme.references.textbooks, enzyme._id)

        carriers = self.carrier_repository.insert(drug.carriers, drug_id)

        for carrier in carriers:
            self.carrier_action_repository.insert(carrier.actions, carrier._id)

            carrier_polypeptide = self.carrier_polypeptide_repository.insert(carrier.polypeptide, carrier._id)
            self.carrier_polypeptide_external_identifier_repository.insert(carrier_polypeptide.external_identifiers, carrier_polypeptide._id)
            self.carrier_polypeptide_go_classifier_repository.insert(carrier_polypeptide.go_classifiers, carrier_polypeptide._id)
            self.carrier_polypeptide_pfam_repository.insert(carrier_polypeptide.pfams, carrier_polypeptide._id)
            self.carrier_polypeptide_synonym_repository.insert(carrier_polypeptide.synonyms, carrier_polypeptide._id)

            self.carrier_reference_article_repository.insert(carrier.references.articles, carrier._id)
            self.carrier_reference_attachment_repository.insert(carrier.references.attachments, carrier._id)
            self.carrier_reference_link_repository.insert(carrier.references.links, carrier._id)
            self.carrier_reference_textbook_repository.insert(carrier.references.textbooks, carrier._id)

        transporters = self.transporter_repository.insert(drug.transporters, drug_id)

        for transporter in transporters:
            self.transporter_action_repository.insert(transporter.actions, transporter._id)

            transporter_polypeptide = self.transporter_polypeptide_repository.insert(transporter.polypeptide, transporter._id)
            self.transporter_polypeptide_external_identifier_repository.insert(transporter_polypeptide.external_identifiers, transporter_polypeptide._id)
            self.transporter_polypeptide_go_classifier_repository.insert(transporter_polypeptide.go_classifiers, transporter_polypeptide._id)
            self.transporter_polypeptide_pfam_repository.insert(transporter_polypeptide.pfams, transporter_polypeptide._id)
            self.transporter_polypeptide_synonym_repository.insert(transporter_polypeptide.synonyms, transporter_polypeptide._id)

            self.transporter_reference_article_repository.insert(transporter.references.articles, transporter._id)
            self.transporter_reference_attachment_repository.insert(transporter.references.attachments, transporter._id)
            self.transporter_reference_link_repository.insert(transporter.references.links, transporter._id)
            self.transporter_reference_textbook_repository.insert(transporter.references.textbooks, transporter._id)

        self.transporter_repository.insert(drug.transporters, drug_id)

        self.mysql_repository.commit_connection()

        print(drug_id)


