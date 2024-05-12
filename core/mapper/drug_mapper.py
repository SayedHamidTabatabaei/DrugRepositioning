import datetime

from _decimal import Decimal
from typing import Optional

from core.domain.article import Article
from core.domain.atc_code import AtcCode
from core.domain.attachment import Attachment
from core.domain.calculated_property import CalculatedProperty
from core.domain.carrier import Carrier
from core.domain.category import Category
from core.domain.classification import Classification
from core.domain.dosage import Dosage
from core.domain.drug import Drug
from core.domain.drug_bank_id import DrugBankId
from core.domain.drug_interaction import DrugInteraction
from core.domain.element import Element
from core.domain.enzyme import Enzyme
from core.domain.go_classifier import GoClassifier
from core.domain.pfam import Pfam
from core.domain.polypeptide import Polypeptide
from core.domain.reaction_enzyme import ReactionEnzyme
from core.domain.experimental_property import ExperimentalProperty
from core.domain.external_identifier import ExternalIdentifier
from core.domain.external_link import ExternalLink
from core.domain.general_references import GeneralReferences
from core.domain.international_brand import InternationalBrand
from core.domain.level import Level
from core.domain.link import Link
from core.domain.manufacturer import Manufacturer
from core.domain.mixture import Mixture
from core.domain.packager import Packager
from core.domain.patent import Patent
from core.domain.pathway import Pathway
from core.domain.pathway_drug import PathwayDrug
from core.domain.price import Price
from core.domain.product import Product
from core.domain.reaction import Reaction
from core.domain.references import References
from core.domain.salt import Salt
from core.domain.sequence import Sequence
from core.domain.snp_adverse_drug_reaction import SnpAdverseDrugReaction
from core.domain.snp_effect import SnpEffect
from core.domain.synonym import Synonym
from core.domain.target import Target
from core.domain.text_book import TextBook
from core.domain.transporter import Transporter


def map_drugbank_id(item):
    value = item.childNodes[0].nodeValue
    primary = False

    for attribute_key, attribute_value in item.attributes._attrs.items():
        if attribute_key == 'primary':
            primary = bool(attribute_value.nodeValue)

        elif attribute_key != '#text':
            print('map_drugbank_id has another attribute params')

    return DrugBankId(value, primary)


def map_groups(item):
    result = []

    for group in item.childNodes:

        if group.nodeName == 'group':
            result.append(group.childNodes[0].nodeValue)

        elif group.nodeName != '#text':
            print('map_groups has another prop params ' + item.nodeName)

    return result


def map_articles(ref):
    result = []

    for article in ref.childNodes:

        if article.nodeName == '#text':
            continue

        ref_id = ''
        pubmed_id = ''
        citation = ''

        for article_item in article.childNodes:
            if len(article_item.childNodes) == 0:
                continue

            if article_item.nodeName == 'ref-id':
                ref_id = article_item.childNodes[0].nodeValue
            elif article_item.nodeName == 'pubmed-id':
                pubmed_id = article_item.childNodes[0].nodeValue
            elif article_item.nodeName == 'citation':
                citation = article_item.childNodes[0].nodeValue

            elif article_item.nodeName != '#text':
                print('map_articles has another prop params ' + article_item.nodeName)

        result.append(Article(ref_id, pubmed_id, citation))

    return result


def map_textbooks(ref):
    result = []

    for textbook in ref.childNodes:

        if textbook.nodeName == '#text':
            continue

        ref_id = ''
        isbn = ''
        citation = ''

        for textbook_item in textbook.childNodes:

            if len(textbook_item.childNodes) == 0:
                continue

            if textbook_item.nodeName == 'ref-id':
                ref_id = textbook_item.childNodes[0].nodeValue
            elif textbook_item.nodeName == 'isbn':
                isbn = textbook_item.childNodes[0].nodeValue
            elif textbook_item.nodeName == 'citation':
                citation = textbook_item.childNodes[0].nodeValue

            elif textbook_item.nodeName != '#text':
                print('map_textbooks has another prop params ' + textbook_item.nodeName)

        result.append(TextBook(ref_id, isbn, citation))

    return result


def map_links(ref):
    result = []

    for link in ref.childNodes:

        if link.nodeName == '#text':
            continue

        ref_id = ''
        title = ''
        url = ''

        for link_item in link.childNodes:
            if link_item.nodeName == 'ref-id':
                ref_id = link_item.childNodes[0].nodeValue
            elif link_item.nodeName == 'title':
                title = link_item.childNodes[0].nodeValue
            elif link_item.nodeName == 'url':
                url = link_item.childNodes[0].nodeValue

            elif link_item.nodeName != '#text':
                print('map_links has another prop params ' + link_item.nodeName)

        result.append(Link(ref_id, title, url))

    return result


def map_attachments(ref):
    result = []

    for attachment in ref.childNodes:

        if attachment.nodeName == '#text':
            continue

        ref_id = ''
        title = ''
        url = ''

        for attachment_item in attachment.childNodes:
            if attachment_item.nodeName == 'ref-id':
                ref_id = attachment_item.childNodes[0].nodeValue
            elif attachment_item.nodeName == 'title':
                title = attachment_item.childNodes[0].nodeValue
            elif attachment_item.nodeName == 'url':
                url = attachment_item.childNodes[0].nodeValue

            elif attachment_item.nodeName != '#text':
                print('map_attachments has another prop params ' + attachment_item.nodeName)

        result.append(Attachment(ref_id, title, url))

    return result


def map_general_references(item):
    result = GeneralReferences()

    for ref in item.childNodes:

        if ref.nodeName == 'articles':
            result.articles = map_articles(ref)

        elif ref.nodeName == 'textbooks':
            result.textbooks = map_textbooks(ref)

        elif ref.nodeName == 'links':
            result.links = map_links(ref)

        elif ref.nodeName == 'attachments':
            result.attachments = map_attachments(ref)

        elif ref.nodeName != '#text':
            print('map_general_references has another prop params ' + item.nodeName)

    return result


def map_classification(item):
    result = Classification()

    for classification in item.childNodes:

        if len(classification.childNodes) == 0:
            continue

        if classification.nodeName == 'description':
            result.description = classification.childNodes[0].nodeValue

        elif classification.nodeName == 'direct-parent':
            result.direct_parent = classification.childNodes[0].nodeValue

        elif classification.nodeName == 'kingdom':
            result.kingdom = classification.childNodes[0].nodeValue

        elif classification.nodeName == 'superclass':
            result.superclass = classification.childNodes[0].nodeValue

        elif classification.nodeName == 'class':
            result.class_category = classification.childNodes[0].nodeValue

        elif classification.nodeName == 'subclass':
            result.subclass = classification.childNodes[0].nodeValue

        elif classification.nodeName == 'alternative-parent':
            result.alternative_parent.append(classification.childNodes[0].nodeValue)

        elif classification.nodeName == 'substituent':
            result.substituent.append(classification.childNodes[0].nodeValue)

        elif classification.nodeName != '#text':
            print('map_classification has another prop params ' + item.nodeName)

    return result


def map_salts(item):
    result = []

    for salt in item.childNodes:

        if salt.nodeName == '#text':
            continue

        drugbank_ids = []
        name = ''
        unii = ''
        cas_number = ''
        inchikey = ''
        average_mass = 0.0
        monoisotopic_mass = 0.0

        for salt_item in salt.childNodes:

            if len(salt_item.childNodes) == 0:
                continue

            if salt_item.nodeName == 'drugbank-id':
                drugbank_ids.append(map_drugbank_id(salt_item))
            elif salt_item.nodeName == 'name':
                name = salt_item.childNodes[0].nodeValue
            elif salt_item.nodeName == 'unii':
                unii = salt_item.childNodes[0].nodeValue
            elif salt_item.nodeName == 'cas-number':
                cas_number = salt_item.childNodes[0].nodeValue
            elif salt_item.nodeName == 'inchikey':
                inchikey = salt_item.childNodes[0].nodeValue
            elif salt_item.nodeName == 'average-mass':
                average_mass = salt_item.childNodes[0].nodeValue
            elif salt_item.nodeName == 'monoisotopic-mass':
                monoisotopic_mass = salt_item.childNodes[0].nodeValue

            elif salt_item.nodeName != '#text':
                print('map_salts has another prop params ' + salt_item.nodeName)

        result.append(Salt(drugbank_ids, name, unii, cas_number, inchikey, average_mass, monoisotopic_mass))

    return result


def map_synonyms(item):
    result = []

    for synonym in item.childNodes:

        if synonym.nodeName == '#text':
            continue

        value = synonym.childNodes[0].nodeValue
        language = ""
        coder = ""

        for attribute_key, attribute_value in synonym.attributes._attrs.items():
            if attribute_key == 'language':
                language = attribute_value.nodeValue
            elif attribute_key == 'coder':
                coder = attribute_value.nodeValue

            elif attribute_key != '#text':
                print('map_synonyms has another attr params')

        result.append(Synonym(value, language, coder))

    return result


def map_products(item):
    result = []

    for product in item.childNodes:

        if product.nodeName == '#text':
            continue

        name = ""
        labeller = ""
        ndc_id = ""
        ndc_product_code = ""
        dpd_id = ""
        ema_product_code = ""
        ema_ma_number = ""
        started_marketing_on = ""
        ended_marketing_on = ""
        dosage_form = ""
        strength = ""
        route = ""
        fda_application_number = ""
        generic = False
        over_the_counter = False
        approved = False
        country = ""
        source = ""

        for product_item in product.childNodes:

            if len(product_item.childNodes) == 0:
                continue

            if product_item.nodeName == 'name':
                name = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'labeller':
                labeller = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'ndc-id':
                ndc_id = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'ndc-product-code':
                ndc_product_code = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'dpd-id':
                dpd_id = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'ema-product-code':
                ema_product_code = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'ema-ma-number':
                ema_ma_number = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'started-marketing-on':
                started_marketing_on = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'ended-marketing-on':
                ended_marketing_on = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'dosage-form':
                dosage_form = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'strength':
                strength = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'route':
                route = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'fda-application-number':
                fda_application_number = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'generic':
                generic = bool(product_item.childNodes[0].nodeValue)
            elif product_item.nodeName == 'over-the-counter':
                over_the_counter = bool(product_item.childNodes[0].nodeValue)
            elif product_item.nodeName == 'approved':
                approved = bool(product_item.childNodes[0].nodeValue)
            elif product_item.nodeName == 'country':
                country = product_item.childNodes[0].nodeValue
            elif product_item.nodeName == 'source':
                source = product_item.childNodes[0].nodeValue

            elif product_item.nodeName != '#text':
                print('map_products has another prop params ' + item.nodeName)

        result.append(
            Product(name, labeller, ndc_id, ndc_product_code, dpd_id, ema_product_code, ema_ma_number,
                    started_marketing_on, ended_marketing_on, dosage_form, strength, route, fda_application_number,
                    generic, over_the_counter, approved, country, source))

    return result


def map_international_brands(item):
    result = []

    for brand in item.childNodes:

        if brand.nodeName == '#text':
            continue

        name = ""
        company = ""

        for brand_item in brand.childNodes:

            if len(brand_item.childNodes) == 0:
                continue

            if brand_item.nodeName == 'name':
                name = brand_item.childNodes[0].nodeValue
            elif brand_item.nodeName == 'company':
                company = brand_item.childNodes[0].nodeValue

            elif brand_item.nodeName != '#text':
                print('map_international_brands has another prop params ' + item.nodeName)

        result.append(InternationalBrand(name, company))

    return result


def map_mixtures(item):
    result = []

    for mixture in item.childNodes:

        if mixture.nodeName == '#text':
            continue

        name = ""
        ingredients = ""

        for mixture_item in mixture.childNodes:

            if len(mixture_item.childNodes) == 0:
                continue

            if mixture_item.nodeName == 'name':
                name = mixture_item.childNodes[0].nodeValue
            elif mixture_item.nodeName == 'ingredients':
                ingredients = mixture_item.childNodes[0].nodeValue

            elif mixture_item.nodeName != '#text':
                print('map_mixtures has another prop params ' + item.nodeName)

        result.append(Mixture(name, ingredients))

    return result


def map_packagers(item):
    result = []
    for packager in item.childNodes:

        if packager.nodeName == '#text':
            continue

        name = ""
        ingredients = ""

        for packager_item in packager.childNodes:

            if len(packager_item.childNodes) == 0:
                continue

            if packager_item.nodeName == 'name':
                name = packager_item.childNodes[0].nodeValue
            elif packager_item.nodeName == 'url':
                ingredients = packager_item.childNodes[0].nodeValue

            elif packager_item.nodeName != '#text':
                print('map_packagers has another prop params ' + item.nodeName)

        result.append(Packager(name, ingredients))

    return result


def map_manufacturers(item):
    result = []
    for manufacturer in item.childNodes:

        if manufacturer.nodeName == '#text':
            continue

        value = manufacturer.childNodes[0].nodeValue
        generic = ""
        url = ""

        for attribute_key, attribute_value in manufacturer.attributes._attrs.items():
            if attribute_key == 'generic':
                generic = attribute_value.nodeValue
            elif attribute_key == 'url':
                url = attribute_value.nodeValue

            elif attribute_key != '#text':
                print('map_manufacturers has another attr params')

        result.append(Manufacturer(value, generic, url))

    return result


def map_prices(item):
    result = []

    for price in item.childNodes:

        if price.nodeName == '#text':
            continue

        description = ''
        cost = 0.0
        currency = ''
        unit = ''

        for price_item in price.childNodes:

            if len(price_item.childNodes) == 0:
                continue

            if price_item.nodeName == 'description':
                description = price_item.childNodes[0].nodeValue
            elif price_item.nodeName == 'cost':
                cost = Decimal(price_item.childNodes[0].nodeValue)

                for attribute_key, attribute_value in price_item.attributes._attrs.items():
                    if attribute_key == 'currency':
                        currency = attribute_value.nodeValue

                    elif attribute_key != '#text':
                        print('map_prices has another attr params')

            elif price_item.nodeName == 'unit':
                unit = price_item.childNodes[0].nodeValue

            elif price_item.nodeName != '#text':
                print('map_prices has another prop params ' + item.nodeName)

        result.append(Price(description, cost, currency, unit))

    return result


def map_categories(item):
    result = []

    for category in item.childNodes:

        if category.nodeName == '#text':
            continue

        category_prop = ""
        mesh_id = ""

        for category_item in category.childNodes:

            if len(category_item.childNodes) == 0:
                continue

            if category_item.nodeName == 'category':
                category_prop = category_item.childNodes[0].nodeValue
            elif category_item.nodeName == 'mesh-id':
                mesh_id = category_item.childNodes[0].nodeValue

            elif category_item.nodeName != '#text':
                print('map_categories has another prop params ' + item.nodeName)

        result.append(Category(category_prop, mesh_id))

    return result


def map_affected_organisms(item):
    result = []

    for affected_organism in item.childNodes:

        if affected_organism.nodeName == 'affected-organism':
            result.append(affected_organism.childNodes[0].nodeValue)

        elif affected_organism.nodeName != '#text':
            print('map_affected_organisms has another prop params ' + item.nodeName)

    return result


def map_dosages(item):
    result = []

    for dosage in item.childNodes:

        if dosage.nodeName == '#text':
            continue

        form = ""
        route = ""
        strength = ""

        for dosage_item in dosage.childNodes:

            if len(dosage_item.childNodes) == 0:
                continue

            if dosage_item.nodeName == 'form':
                form = dosage_item.childNodes[0].nodeValue
            elif dosage_item.nodeName == 'route':
                route = dosage_item.childNodes[0].nodeValue
            elif dosage_item.nodeName == 'strength':
                strength = dosage_item.childNodes[0].nodeValue

            elif dosage_item.nodeName != '#text':
                print('map_dosages has another prop params ' + item.nodeName)

        result.append(Dosage(form, route, strength))

    return result


def map_atc_codes(item):
    result = []

    for atc_code in item.childNodes:

        if atc_code.nodeName == '#text':
            continue

        code = ''
        levels = []

        for attribute_key, attribute_value in atc_code.attributes._attrs.items():
            if attribute_key == 'code':
                code = attribute_value.nodeValue

            elif attribute_key != '#text':
                print('map_atc_codes has another attr params')

        for level in atc_code.childNodes:

            if level.nodeName == '#text':
                continue

            level_code = ''
            value = level.childNodes[0].nodeValue

            for attribute_key, attribute_value in level.attributes._attrs.items():
                if attribute_key == 'code':
                    level_code = attribute_value.nodeValue

                elif attribute_key != '#text':
                    print('map_atc_codes has another attr params')

            levels.append(Level(value, level_code))

        result.append(AtcCode(code, levels))

    return result


def map_pdb_entries(item):
    result = []

    for pdb_entry in item.childNodes:

        if pdb_entry.nodeName == 'pdb-entry':
            result.append(pdb_entry.childNodes[0].nodeValue)

        elif pdb_entry.nodeName != '#text':
            print('map_pdb_entries has another prop params ' + item.nodeName)

    return result


def map_patents(item):
    result = []

    for patent in item.childNodes:

        if patent.nodeName == '#text':
            continue

        number = 0
        country = ""
        approved = datetime.MINYEAR
        expires = datetime.MINYEAR
        pediatric_extension = False

        for patent_item in patent.childNodes:

            if len(patent_item.childNodes) == 0:
                continue

            if patent_item.nodeName == 'number':
                number = patent_item.childNodes[0].nodeValue
            elif patent_item.nodeName == 'country':
                country = patent_item.childNodes[0].nodeValue
            elif patent_item.nodeName == 'approved':
                approved = patent_item.childNodes[0].nodeValue
            elif patent_item.nodeName == 'expires':
                expires = patent_item.childNodes[0].nodeValue
            elif patent_item.nodeName == 'pediatric-extension':
                pediatric_extension = bool(patent_item.childNodes[0].nodeValue)

            elif patent_item.nodeName != '#text':
                print('map_patents has another prop params ' + item.nodeName)

        result.append(Patent(number, country, approved, expires, pediatric_extension))

    return result


def map_food_interactions(item):
    result = []

    for food_interaction in item.childNodes:

        if food_interaction.nodeName == 'food-interaction':
            result.append(food_interaction.childNodes[0].nodeValue)

        elif food_interaction.nodeName != '#text':
            print('map_food_interactions has another prop params ' + item.nodeName)

    return result


def map_drug_interactions(item):
    result = []

    for drug_interaction in item.childNodes:

        if drug_interaction.nodeName == '#text':
            continue

        drugbank_id = ''
        name = ''
        description = ''

        for drug_interaction_item in drug_interaction.childNodes:

            if len(drug_interaction_item.childNodes) == 0:
                continue

            if drug_interaction_item.nodeName == 'drugbank-id':
                drugbank_id = drug_interaction_item.childNodes[0].nodeValue
            elif drug_interaction_item.nodeName == 'name':
                name = drug_interaction_item.childNodes[0].nodeValue
            elif drug_interaction_item.nodeName == 'description':
                description = drug_interaction_item.childNodes[0].nodeValue

            elif drug_interaction_item.nodeName != '#text':
                print('map_drug_interactions has another prop params ' + item.nodeName)

        result.append(DrugInteraction(drugbank_id, name, description))

    return result


def map_calculated_properties(item):
    result = []

    for calculated_property in item.childNodes:

        if calculated_property.nodeName == '#text':
            continue

        kind = ''
        value = 0.0
        source = ''

        for calculated_property_item in calculated_property.childNodes:

            if len(calculated_property_item.childNodes) == 0:
                continue

            if calculated_property_item.nodeName == 'kind':
                kind = calculated_property_item.childNodes[0].nodeValue
            elif calculated_property_item.nodeName == 'value':
                value = calculated_property_item.childNodes[0].nodeValue
            elif calculated_property_item.nodeName == 'source':
                source = calculated_property_item.childNodes[0].nodeValue

            elif calculated_property_item.nodeName != '#text':
                print('map_calculated_properties has another prop params ' + calculated_property_item.nodeName)

        result.append(CalculatedProperty(kind, value, source))

    return result


def map_sequences(item):
    result = []

    for sequence in item.childNodes:

        if sequence.nodeName == '#text':
            continue

        value = sequence.childNodes[0].nodeValue
        sequence_format = ""

        for attribute_key, attribute_value in sequence.attributes._attrs.items():
            if attribute_key == 'format':
                sequence_format = attribute_value.nodeValue

            elif attribute_key != '#text':
                print('map_sequences has another attr params')

        result.append(Sequence(value, sequence_format))

    return result


def map_experimental_properties(item):
    result = []

    for experimental_property in item.childNodes:

        if experimental_property.nodeName == '#text':
            continue

        kind = ''
        value = ''
        source = ''

        for experimental_property_item in experimental_property.childNodes:

            if len(experimental_property_item.childNodes) == 0:
                continue

            if experimental_property_item.nodeName == 'kind':
                kind = experimental_property_item.childNodes[0].nodeValue
            elif experimental_property_item.nodeName == 'value':
                value = experimental_property_item.childNodes[0].nodeValue
            elif experimental_property_item.nodeName == 'source':
                source = experimental_property_item.childNodes[0].nodeValue

            elif experimental_property_item.nodeName != '#text':
                print('map_experimental_properties has another prop params ' + item.nodeName)

        result.append(ExperimentalProperty(kind, value, source))

    return result


def map_external_identifiers(item):
    result = []

    for external_identifier in item.childNodes:

        if external_identifier.nodeName == '#text':
            continue

        resource = ''
        identifier = ''

        for external_identifier_item in external_identifier.childNodes:

            if len(external_identifier_item.childNodes) == 0:
                continue

            if external_identifier_item.nodeName == 'resource':
                resource = external_identifier_item.childNodes[0].nodeValue
            elif external_identifier_item.nodeName == 'identifier':
                identifier = external_identifier_item.childNodes[0].nodeValue

            elif external_identifier_item.nodeName != '#text':
                print('map_external_identifiers has another prop params ' + item.nodeName)

        result.append(ExternalIdentifier(resource, identifier))

    return result


def map_external_links(item):
    result = []

    for external_link in item.childNodes:

        if external_link.nodeName == '#text':
            continue

        resource = ''
        url = ''

        for external_link_item in external_link.childNodes:

            if len(external_link_item.childNodes) == 0:
                continue

            if external_link_item.nodeName == 'resource':
                resource = external_link_item.childNodes[0].nodeValue
            elif external_link_item.nodeName == 'url':
                url = external_link_item.childNodes[0].nodeValue

            elif external_link_item.nodeName != '#text':
                print('map_external_links has another prop params ' + item.nodeName)

        result.append(ExternalLink(resource, url))

    return result


def map_pathway_drugs(item):
    result = []

    for pathway_drug in item.childNodes:

        if pathway_drug.nodeName == '#text':
            continue

        drugbank_id = ''
        name = ''

        for pathway_drug_item in pathway_drug.childNodes:

            if len(pathway_drug_item.childNodes) == 0:
                continue

            if pathway_drug_item.nodeName == 'drugbank-id':
                drugbank_id = pathway_drug_item.childNodes[0].nodeValue
            elif pathway_drug_item.nodeName == 'name':
                name = pathway_drug_item.childNodes[0].nodeValue

            elif pathway_drug_item.nodeName != '#text':
                print('map_pathway_drugs has another prop params ' + item.nodeName)

        result.append(PathwayDrug(drugbank_id, name))

    return result


def map_pathway_enzymes(item):
    result = []

    for uniprot_id in item.childNodes:

        if uniprot_id.nodeName == 'uniprot-id':
            result.append(uniprot_id.childNodes[0].nodeValue)

        elif uniprot_id.nodeName != '#text':
            print('map_pathway_enzymes has another prop params ' + item.nodeName)

    return result


def map_pathways(item):
    result = []

    for pathway in item.childNodes:

        if pathway.nodeName == '#text':
            continue

        smpdb_id = ""
        name = ""
        category = ""
        drugs = []
        enzymes = []

        for pathway_item in pathway.childNodes:

            if len(pathway_item.childNodes) == 0:
                continue

            if pathway_item.nodeName == 'smpdb-id':
                smpdb_id = pathway_item.childNodes[0].nodeValue
            elif pathway_item.nodeName == 'name':
                name = pathway_item.childNodes[0].nodeValue
            elif pathway_item.nodeName == 'category':
                category = pathway_item.childNodes[0].nodeValue
            elif pathway_item.nodeName == 'drugs':
                drugs = map_pathway_drugs(pathway_item)
            elif pathway_item.nodeName == 'enzymes':
                enzymes = map_pathway_enzymes(pathway_item)

            elif pathway_item.nodeName != '#text':
                print('map_pathways has another prop params ' + item.nodeName)

        result.append(Pathway(smpdb_id, name, category, drugs, enzymes))

    return result


def map_element(item):
    drugbank_id = ''
    name = ''

    for element in item.childNodes:

        if len(element.childNodes) == 0:
            continue

        if element.nodeName == 'drugbank-id':
            drugbank_id = element.childNodes[0].nodeValue

        elif element.nodeName == 'name':
            name = element.childNodes[0].nodeValue

        elif element.nodeName != '#text':
            print('map_element has another prop params ' + item.nodeName)

    return Element(drugbank_id, name)


def map_reaction_enzymes(item):
    result = []

    for enzyme in item.childNodes:

        if enzyme.nodeName == '#text':
            continue

        drugbank_id = ''
        name = ''
        uniprot_id = ''

        for enzyme_item in enzyme.childNodes:

            if len(enzyme_item.childNodes) == 0:
                continue

            if enzyme_item.nodeName == 'drugbank-id':
                drugbank_id = enzyme_item.childNodes[0].nodeValue
            elif enzyme_item.nodeName == 'name':
                name = enzyme_item.childNodes[0].nodeValue
            elif enzyme_item.nodeName == 'uniprot-id':
                uniprot_id = enzyme_item.childNodes[0].nodeValue

            elif enzyme_item.nodeName != '#text':
                print('map_reaction_enzymes has another prop params ' + item.nodeName)

        result.append(ReactionEnzyme(drugbank_id, name, uniprot_id))

    return result


def map_reactions(item):
    result = []

    for reaction in item.childNodes:

        if reaction.nodeName == '#text':
            continue

        sequence: int = 0
        left_element: Optional[Element] = None
        right_element: Optional[Element] = None
        enzymes = []

        for reaction_item in reaction.childNodes:

            if len(reaction_item.childNodes) == 0:
                continue

            if reaction_item.nodeName == 'sequence':
                sequence = int(reaction_item.childNodes[0].nodeValue)
            elif reaction_item.nodeName == 'left-element':
                left_element = map_element(reaction_item)
            elif reaction_item.nodeName == 'right-element':
                right_element = map_element(reaction_item)
            elif reaction_item.nodeName == 'enzymes':
                enzymes = map_reaction_enzymes(reaction_item)

            elif reaction_item.nodeName != '#text':
                print('map_reactions has another prop params ' + item.nodeName)

        result.append(Reaction(sequence, left_element, right_element, enzymes))

    return result


def map_snp_effects(item):
    result = []

    for effect in item.childNodes:

        if effect.nodeName == '#text':
            continue

        protein_name = ''
        gene_symbol = ''
        uniprot_id = ''
        rs_id = ''
        allele = ''
        defining_change = ''
        description = ''
        pubmed_id = ''

        for effect_item in effect.childNodes:

            if len(effect_item.childNodes) == 0:
                continue

            if effect_item.nodeName == 'protein-name':
                protein_name = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'gene-symbol':
                gene_symbol = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'uniprot-id':
                uniprot_id = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'rs-id':
                rs_id = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'allele':
                allele = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'defining-change':
                defining_change = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'description':
                description = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'pubmed-id':
                pubmed_id = effect_item.childNodes[0].nodeValue

            elif effect_item.nodeName != '#text':
                print('map_snp_effects has another prop params ' + item.nodeName)

        result.append(
            SnpEffect(protein_name, gene_symbol, uniprot_id, rs_id, allele, defining_change, description, pubmed_id))

    return result


def map_snp_adverse_drug_reactions(item):
    result = []

    for effect in item.childNodes:

        if effect.nodeName == '#text':
            continue

        protein_name = ''
        gene_symbol = ''
        uniprot_id = ''
        rs_id = ''
        allele = ''
        adverse_reaction = ''
        description = ''
        pubmed_id = ''

        for effect_item in effect.childNodes:

            if len(effect_item.childNodes) == 0:
                continue

            if effect_item.nodeName == 'protein-name':
                protein_name = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'gene-symbol':
                gene_symbol = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'uniprot-id':
                uniprot_id = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'rs-id':
                rs_id = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'allele':
                allele = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'adverse-reaction':
                adverse_reaction = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'description':
                description = effect_item.childNodes[0].nodeValue
            elif effect_item.nodeName == 'pubmed-id':
                pubmed_id = effect_item.childNodes[0].nodeValue

            elif effect_item.nodeName != '#text':
                print('map_snp_adverse_drug_reactions has another prop params ' + item.nodeName)

        result.append(
            SnpAdverseDrugReaction(protein_name, gene_symbol, uniprot_id, rs_id, allele, adverse_reaction, description,
                                   pubmed_id))

    return result


def map_actions(item):
    result = []

    for action in item.childNodes:

        if action.nodeName == 'action':
            result.append(action.childNodes[0].nodeValue)

        elif action.nodeName != '#text':
            print('map_actions has another prop params ' + item.nodeName)

    return result


def map_references(item):
    result = References()

    for ref in item.childNodes:

        if ref.nodeName == 'articles':
            result.articles = map_articles(ref)

        elif ref.nodeName == 'textbooks':
            result.textbooks = map_textbooks(ref)

        elif ref.nodeName == 'links':
            result.links = map_links(ref)

        elif ref.nodeName == 'attachments':
            result.attachments = map_attachments(ref)

        elif ref.nodeName != '#text':
            print('map_references has another prop params ' + item.nodeName)

    return result


def map_pfams(item):
    result = []

    for pfam in item.childNodes:

        if pfam.nodeName == '#text':
            continue

        identifier = ''
        name = ''

        for pfam_item in pfam.childNodes:

            if len(pfam_item.childNodes) == 0:
                continue

            if pfam_item.nodeName == 'identifier':
                identifier = pfam_item.childNodes[0].nodeValue
            elif pfam_item.nodeName == 'name':
                name = pfam_item.childNodes[0].nodeValue

            elif pfam_item.nodeName != '#text':
                print('map_pfams has another prop params ' + item.nodeName)

        result.append(Pfam(identifier, name))

    return result


def map_go_classifiers(item):
    result = []

    for go_classifier in item.childNodes:

        if go_classifier.nodeName == '#text':
            continue

        category = ''
        description = ''

        for go_classifier_item in go_classifier.childNodes:

            if len(go_classifier_item.childNodes) == 0:
                continue

            if go_classifier_item.nodeName == 'category':
                category = go_classifier_item.childNodes[0].nodeValue
            elif go_classifier_item.nodeName == 'description':
                description = go_classifier_item.childNodes[0].nodeValue

            elif go_classifier_item.nodeName != '#text':
                print('map_go_classifiers has another prop params ' + item.nodeName)

        result.append(GoClassifier(category, description))

    return result


def map_polypeptide(item):
    _id = ''
    source = ''
    name = ''
    general_function = ''
    specific_function = ''
    gene_name = ''
    locus = ''
    cellular_location = ''
    transmembrane_regions = ''
    signal_regions = ''
    theoretical_pi = 0.0
    molecular_weight = 0.0
    chromosome_location = 0
    organism_ncbi_taxonomy_id = None
    organism_ncbi_taxonomy_value = ''
    external_identifiers = []
    synonyms = []
    amino_acid_sequence_format = ''
    amino_acid_sequence_value = ''
    gene_sequence_format = ''
    gene_sequence_value = ''
    pfams = []
    go_classifiers = []

    for attribute_key, attribute_value in item.attributes._attrs.items():
        if attribute_key == 'id':
            _id = attribute_value.nodeValue
        elif attribute_key == 'source':
            source = attribute_value.nodeValue

        elif attribute_key != '#text':
            print('map_polypeptide has another attr params')

    for polypeptide_item in item.childNodes:

        if len(polypeptide_item.childNodes) == 0:
            continue

        if polypeptide_item.nodeName == 'name':
            name = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'general-function':
            general_function = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'specific-function':
            specific_function = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'gene-name':
            gene_name = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'locus':
            locus = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'cellular-location':
            cellular_location = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'transmembrane-regions':
            transmembrane_regions = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'signal-regions':
            signal_regions = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'theoretical-pi':
            theoretical_pi = Decimal(polypeptide_item.childNodes[0].nodeValue)

        elif polypeptide_item.nodeName == 'molecular-weight':
            molecular_weight = Decimal(polypeptide_item.childNodes[0].nodeValue)

        elif polypeptide_item.nodeName == 'chromosome-location':
            chromosome_location = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'organism':
            for attribute_key, attribute_value in polypeptide_item.attributes._attrs.items():
                if attribute_key == 'ncbi-taxonomy-id':
                    if attribute_value.nodeValue.isdigit():
                        organism_ncbi_taxonomy_id = attribute_value.nodeValue
                    else:
                        organism_ncbi_taxonomy_id = None

                elif attribute_key != '#text':
                    print('map_polypeptide has another attr params')

            organism_ncbi_taxonomy_value = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'external-identifiers':
            external_identifiers = map_external_identifiers(polypeptide_item)

        elif polypeptide_item.nodeName == 'synonyms':
            synonyms = map_synonyms(polypeptide_item)

        elif polypeptide_item.nodeName == 'amino-acid-sequence':
            for attribute_key, attribute_value in polypeptide_item.attributes._attrs.items():
                if attribute_key == 'format':
                    amino_acid_sequence_format = attribute_value.nodeValue

                elif attribute_key != '#text':
                    print('map_polypeptide has another attr params')

            amino_acid_sequence_value = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'gene-sequence':
            for attribute_key, attribute_value in polypeptide_item.attributes._attrs.items():
                if attribute_key == 'format':
                    gene_sequence_format = attribute_value.nodeValue

                elif attribute_key != '#text':
                    print('map_polypeptide has another attr params')

            gene_sequence_value = polypeptide_item.childNodes[0].nodeValue

        elif polypeptide_item.nodeName == 'pfams':
            pfams = map_pfams(polypeptide_item)

        elif polypeptide_item.nodeName == 'go-classifiers':
            go_classifiers = map_go_classifiers(polypeptide_item)

        elif polypeptide_item.nodeName != '#text':
            print('map_polypeptide has another prop params ' + item.nodeName)

    result = Polypeptide(_id, source, name, general_function, specific_function, gene_name, locus, cellular_location,
                         transmembrane_regions, signal_regions, theoretical_pi, molecular_weight, chromosome_location,
                         organism_ncbi_taxonomy_id, organism_ncbi_taxonomy_value, external_identifiers, synonyms,
                         amino_acid_sequence_format, amino_acid_sequence_value, gene_sequence_format,
                         gene_sequence_value, pfams, go_classifiers)

    return result


def map_targets(item):
    result = []

    for target in item.childNodes:

        if target.nodeName == '#text':
            continue

        position = 0
        _id = ''
        name = ''
        organism = ''
        actions = []
        references = []
        known_action = ''
        polypeptide = Polypeptide

        for attribute_key, attribute_value in target.attributes._attrs.items():
            if attribute_key == 'position':
                position = int(attribute_value.nodeValue)

            elif attribute_key != '#text':
                print('map_targets has another attr params')

        for target_item in target.childNodes:

            if len(target_item.childNodes) == 0:
                continue

            if target_item.nodeName == 'id':
                _id = target_item.childNodes[0].nodeValue
            elif target_item.nodeName == 'name':
                name = target_item.childNodes[0].nodeValue
            elif target_item.nodeName == 'organism':
                organism = target_item.childNodes[0].nodeValue
            elif target_item.nodeName == 'actions':
                actions = map_actions(target_item)
            elif target_item.nodeName == 'references':
                references = map_references(target_item)
            elif target_item.nodeName == 'known-action':
                known_action = target_item.childNodes[0].nodeValue
            elif target_item.nodeName == 'polypeptide':
                polypeptide = map_polypeptide(target_item)

            elif target_item.nodeName != '#text':
                print('map_targets has another prop params ' + item.nodeName)

        result.append(Target(position, _id, name, organism, actions, references, known_action, polypeptide))

    return result


def map_enzymes(item):
    result = []

    for enzyme in item.childNodes:

        if enzyme.nodeName == '#text':
            continue

        position = 0
        _id = ''
        name = ''
        organism = ''
        actions = []
        references = []
        known_action = ''
        polypeptide = Polypeptide
        inhibition_strength = ''
        induction_strength = ''

        for attribute_key, attribute_value in enzyme.attributes._attrs.items():
            if attribute_key == 'position':
                position = int(attribute_value.nodeValue)

            elif attribute_key != '#text':
                print('map_enzymes has another attr params')

        for enzyme_item in enzyme.childNodes:

            if len(enzyme_item.childNodes) == 0:
                continue

            if enzyme_item.nodeName == 'id':
                _id = enzyme_item.childNodes[0].nodeValue
            elif enzyme_item.nodeName == 'name':
                name = enzyme_item.childNodes[0].nodeValue
            elif enzyme_item.nodeName == 'organism':
                organism = enzyme_item.childNodes[0].nodeValue
            elif enzyme_item.nodeName == 'actions':
                actions = map_actions(enzyme_item)
            elif enzyme_item.nodeName == 'references':
                references = map_references(enzyme_item)
            elif enzyme_item.nodeName == 'known-action':
                known_action = enzyme_item.childNodes[0].nodeValue
            elif enzyme_item.nodeName == 'polypeptide':
                polypeptide = map_polypeptide(enzyme_item)
            elif enzyme_item.nodeName == 'inhibition-strength':
                inhibition_strength = enzyme_item.childNodes[0].nodeValue
            elif enzyme_item.nodeName == 'induction-strength':
                induction_strength = enzyme_item.childNodes[0].nodeValue

            elif enzyme_item.nodeName != '#text':
                print('map_enzymes has another prop params ' + item.nodeName)

        result.append(
            Enzyme(position, _id, name, organism, actions, references, known_action, polypeptide, inhibition_strength,
                   induction_strength))

    return result


def map_carriers(item):
    result = []

    for carrier in item.childNodes:

        if carrier.nodeName == '#text':
            continue

        position = 0
        _id = ''
        name = ''
        organism = ''
        actions = []
        references = []
        known_action = ''
        polypeptide = Polypeptide

        for attribute_key, attribute_value in carrier.attributes._attrs.items():
            if attribute_key == 'position':
                position = int(attribute_value.nodeValue)

            elif attribute_key != '#text':
                print('map_carriers has another attr params')

        for carrier_item in carrier.childNodes:

            if len(carrier_item.childNodes) == 0:
                continue

            if carrier_item.nodeName == 'id':
                _id = carrier_item.childNodes[0].nodeValue
            elif carrier_item.nodeName == 'name':
                name = carrier_item.childNodes[0].nodeValue
            elif carrier_item.nodeName == 'organism':
                organism = carrier_item.childNodes[0].nodeValue
            elif carrier_item.nodeName == 'actions':
                actions = map_actions(carrier_item)
            elif carrier_item.nodeName == 'references':
                references = map_references(carrier_item)
            elif carrier_item.nodeName == 'known-action':
                known_action = carrier_item.childNodes[0].nodeValue
            elif carrier_item.nodeName == 'polypeptide':
                polypeptide = map_polypeptide(carrier_item)

            elif carrier_item.nodeName != '#text':
                print('map_carriers has another prop params ' + item.nodeName)

        result.append(Carrier(position, _id, name, organism, actions, references, known_action, polypeptide))

    return result


def map_transporters(item):
    result = []

    for transporter in item.childNodes:

        if transporter.nodeName == '#text':
            continue

        position = 0
        _id = ''
        name = ''
        organism = ''
        actions = []
        references = []
        known_action = ''
        polypeptide = Polypeptide

        for attribute_key, attribute_value in transporter.attributes._attrs.items():
            if attribute_key == 'position':
                position = int(attribute_value.nodeValue)

            elif attribute_key != '#text':
                print('map_transporters has another attr params')

        for transporter_item in transporter.childNodes:

            if len(transporter_item.childNodes) == 0:
                continue

            if transporter_item.nodeName == 'id':
                _id = transporter_item.childNodes[0].nodeValue
            elif transporter_item.nodeName == 'name':
                name = transporter_item.childNodes[0].nodeValue
            elif transporter_item.nodeName == 'organism':
                organism = transporter_item.childNodes[0].nodeValue
            elif transporter_item.nodeName == 'actions':
                actions = map_actions(transporter_item)
            elif transporter_item.nodeName == 'references':
                references = map_references(transporter_item)
            elif transporter_item.nodeName == 'known-action':
                known_action = transporter_item.childNodes[0].nodeValue
            elif transporter_item.nodeName == 'polypeptide':
                polypeptide = map_polypeptide(transporter_item)

            elif transporter_item.nodeName != '#text':
                print('map_transporters has another prop params ' + item.nodeName)

        result.append(Transporter(position, _id, name, organism, actions, references, known_action, polypeptide))

    return result


def map_drug(item):

    result = Drug()

    for attribute_key, attribute_value in item.attributes._attrs.items():
        if attribute_key == 'type':
            result.type = attribute_value.nodeValue
        elif attribute_key == 'created':
            result.created = attribute_value.nodeValue
        elif attribute_key == 'updated':
            result.updated = attribute_value.nodeValue

        elif attribute_key != '#text':
            print('map_polypeptide has another attr params')

    for child_node in item.childNodes:
        if len(child_node.childNodes) == 0:
            continue

        match child_node.nodeName:
            case 'drugbank-id':
                result.drugbank_ids.append(map_drugbank_id(child_node))
            case 'name':
                result.name = child_node.childNodes[0].nodeValue

            case 'description':
                result.description = child_node.childNodes[0].nodeValue

            case 'cas-number':
                result.cas_number = child_node.childNodes[0].nodeValue

            case 'unii':
                result.unii = child_node.childNodes[0].nodeValue

            case 'average-mass':
                result.average_mass = Decimal(child_node.childNodes[0].nodeValue)

            case 'monoisotopic-mass':
                result.monoisotopic_mass = Decimal(child_node.childNodes[0].nodeValue)

            case 'state':
                result.state = child_node.childNodes[0].nodeValue

            case 'groups':
                result.groups = map_groups(child_node)

            case 'general-references':
                result.general_references = map_general_references(child_node)

            case 'synthesis-reference':
                result.synthesis_reference = child_node.childNodes[0].nodeValue

            case 'indication':
                result.indication = child_node.childNodes[0].nodeValue

            case 'pharmacodynamics':
                result.pharmacodynamics = child_node.childNodes[0].nodeValue

            case 'mechanism-of-action':
                result.mechanism_of_action = child_node.childNodes[0].nodeValue

            case 'toxicity':
                result.toxicity = child_node.childNodes[0].nodeValue

            case 'metabolism':
                result.metabolism = child_node.childNodes[0].nodeValue

            case 'absorption':
                result.absorption = child_node.childNodes[0].nodeValue

            case 'half-life':
                result.half_life = child_node.childNodes[0].nodeValue

            case 'protein-binding':
                result.protein_binding = child_node.childNodes[0].nodeValue

            case 'route-of-elimination':
                result.route_of_elimination = child_node.childNodes[0].nodeValue

            case 'volume-of-distribution':
                result.volume_of_distribution = child_node.childNodes[0].nodeValue

            case 'clearance':
                result.clearance = child_node.childNodes[0].nodeValue

            case 'classification':
                result.classification = map_classification(child_node)

            case 'salts':
                result.salts = map_salts(child_node)

            case 'synonyms':
                result.synonyms = map_synonyms(child_node)

            case 'products':
                result.products = map_products(child_node)

            case 'international-brands':
                result.international_brands = map_international_brands(child_node)

            case 'mixtures':
                result.mixtures = map_mixtures(child_node)

            case 'packagers':
                result.packagers = map_packagers(child_node)

            case 'manufacturers':
                result.manufacturers = map_manufacturers(child_node)

            case 'prices':
                result.prices = map_prices(child_node)

            case 'categories':
                result.categories = map_categories(child_node)

            case 'affected-organisms':
                result.affected_organisms = map_affected_organisms(child_node)

            case 'dosages':
                result.dosages = map_dosages(child_node)

            case 'atc-codes':
                result.atc_codes = map_atc_codes(child_node)

            case 'ahfs-codes':
                print('ahfs-codes has issue')

            case 'pdb-entries':
                result.pdb_entries = map_pdb_entries(child_node)

            case 'fda-label':
                result.fda_label = child_node.childNodes[0].nodeValue

            case 'msds':
                result.msds = child_node.childNodes[0].nodeValue

            case 'patents':
                result.patents = map_patents(child_node)

            case 'food-interactions':
                result.food_interactions = map_food_interactions(child_node)

            case 'drug-interactions':
                result.drug_interactions = map_drug_interactions(child_node)

            case 'calculated-properties':
                result.calculated_properties = map_calculated_properties(child_node)

            case 'sequences':
                result.sequences = map_sequences(child_node)

            case 'experimental-properties':
                result.experimental_properties = map_experimental_properties(child_node)

            case 'external-identifiers':
                result.external_identifiers = map_external_identifiers(child_node)

            case 'external-links':
                result.external_links = map_external_links(child_node)

            case 'pathways':
                result.pathways = map_pathways(child_node)

            case 'reactions':
                result.reactions = map_reactions(child_node)

            case 'snp-effects':
                result.snp_effects = map_snp_effects(child_node)

            case 'snp-adverse-drug-reactions':
                result.snp_adverse_drug_reactions = map_snp_adverse_drug_reactions(child_node)

            case 'targets':
                result.targets = map_targets(child_node)

            case 'enzymes':
                result.enzymes = map_enzymes(child_node)

            case 'carriers':
                result.carriers = map_carriers(child_node)

            case 'transporters':
                result.transporters = map_transporters(child_node)

            case _:
                if child_node is not None and child_node.nodeName != '#text':
                    print('map_drug has another prop params ' + child_node.nodeName)

    return result
