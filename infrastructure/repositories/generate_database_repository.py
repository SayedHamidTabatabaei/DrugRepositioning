from infrastructure.mysqldb.mysql_repository import MySqlRepository


class GenerateDatabaseRepository(MySqlRepository):
    def __init__(self):
        super().__init__()

    def generate_database(self):
        super().create_database()

        self.create_drug()

        self.create_drugbank_ids()

        self.create_groups()

        self.create_general_references_articles()

        self.create_general_references_textbooks()

        self.create_general_references_links()

        self.create_general_references_attachments()

        self.create_alternative_parents()

        self.create_substituents()

        self.create_salts()

        self.create_salt_drugbank_ids()

        self.create_synonyms()

        self.create_products()

        self.create_international_brands()

        self.create_mixtures()

        self.create_packagers()

        self.create_manufacturers()

        self.create_prices()

        self.create_categories()

        self.create_affected_organisms()

        self.create_dosages()

        self.create_atc_codes()

        self.create_levels()

        self.create_pdb_entries()

        self.create_patents()

        self.create_food_interactions()

        self.create_drug_interactions()

        self.create_calculated_properties()

        self.create_sequences()

        self.create_experimental_properties()

        self.create_external_identifiers()

        self.create_external_links()

        self.create_pathways()

        self.create_pathway_drugs()

        self.create_pathway_enzymes()

        self.create_reactions()

        self.create_elements()

        self.create_reaction_enzymes()

        self.create_snp_effects()

        self.create_snp_adverse_drug_reactions()

        self.create_targets()

        self.create_target_actions()

        self.create_target_references_articles()

        self.create_target_references_textbooks()

        self.create_target_references_links()

        self.create_target_references_attachments()

        self.create_target_polypeptides()

        self.create_target_polypeptide_external_identifiers()

        self.create_target_polypeptide_synonyms()

        self.create_target_polypeptide_pfams()

        self.create_target_polypeptide_go_classifiers()

        self.create_enzymes()

        self.create_enzyme_actions()

        self.create_enzyme_references_articles()

        self.create_enzyme_references_textbooks()

        self.create_enzyme_references_links()

        self.create_enzyme_references_attachments()

        self.create_enzyme_polypeptides()

        self.create_enzyme_polypeptide_external_identifiers()

        self.create_enzyme_polypeptide_synonyms()

        self.create_enzyme_polypeptide_pfams()

        self.create_enzyme_polypeptide_go_classifiers()

        self.create_carriers()

        self.create_carrier_actions()

        self.create_carrier_references_articles()

        self.create_carrier_references_textbooks()

        self.create_carrier_references_links()

        self.create_carrier_references_attachments()

        self.create_carrier_polypeptides()

        self.create_carrier_polypeptide_external_identifiers()

        self.create_carrier_polypeptide_synonyms()

        self.create_carrier_polypeptide_pfams()

        self.create_carrier_polypeptide_go_classifiers()

        self.create_transporters()

        self.create_transporter_actions()

        self.create_transporter_references_articles()

        self.create_transporter_references_textbooks()

        self.create_transporter_references_links()

        self.create_transporter_references_attachments()

        self.create_transporter_polypeptides()

        self.create_transporter_polypeptide_external_identifiers()

        self.create_transporter_polypeptide_synonyms()

        self.create_transporter_polypeptide_pfams()

        self.create_transporter_polypeptide_go_classifiers()

    def create_drug(self):
        drug_table_script = 'CREATE TABLE drugs (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'name nvarchar(1024),' \
                            'type nvarchar(1024),' \
                            'created_date datetime,' \
                            'updated_date datetime,' \
                            'description text, ' \
                            'cas_number nvarchar(255), ' \
                            'unii nvarchar(255), ' \
                            'average_mass decimal, ' \
                            'monoisotopic_mass decimal, ' \
                            'state nvarchar(255), ' \
                            'synthesis_reference nvarchar(1024), ' \
                            'indication text, ' \
                            'pharmacodynamics text, ' \
                            'mechanism_of_action text, ' \
                            'toxicity text, ' \
                            'metabolism text, ' \
                            'absorption text, ' \
                            'half_life text, ' \
                            'protein_binding text, ' \
                            'route_of_elimination text, ' \
                            'volume_of_distribution text, ' \
                            'clearance text, ' \
                            'classification_description text, ' \
                            'classification_direct_parent nvarchar(255), ' \
                            'classification_kingdom nvarchar(255), ' \
                            'classification_superclass nvarchar(255), ' \
                            'classification_class_category nvarchar(255), ' \
                            'classification_subclass nvarchar(255), ' \
                            'fda_label nvarchar(255), ' \
                            'msds nvarchar(255),' \
                            'PRIMARY KEY (`id`));'

        self.execute_query(drug_table_script)

    def create_drugbank_ids(self):
        drug_table_script = 'CREATE TABLE drugbank_ids (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'drugbank_id nvarchar(255), ' \
                            '`primary` bool, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_drugbank_id FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_groups(self):
        drug_table_script = 'CREATE TABLE `groups` (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_group FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_general_references_articles(self):
        drug_table_script = 'CREATE TABLE general_references_articles (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'ref_id nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_article FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_general_references_textbooks(self):
        drug_table_script = 'CREATE TABLE general_references_textbooks (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'ref_id nvarchar(255), ' \
                            'isbn nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_textbook FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_general_references_links(self):
        drug_table_script = 'CREATE TABLE general_references_links (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_link FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_general_references_attachments(self):
        drug_table_script = 'CREATE TABLE general_references_attachments (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_attachment FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_alternative_parents(self):
        drug_table_script = 'CREATE TABLE alternative_parents (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_alternative_parent FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_substituents(self):
        drug_table_script = 'CREATE TABLE substituents (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_substituent FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_salts(self):
        drug_table_script = 'CREATE TABLE salts (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'name nvarchar(1024), ' \
                            'unii nvarchar(255), ' \
                            'cas_number nvarchar(255), ' \
                            'inchikey nvarchar(255), ' \
                            'average_mass decimal, ' \
                            'monoisotopic_mass decimal, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_salt FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_salt_drugbank_ids(self):
        drug_table_script = 'CREATE TABLE salt_drugbank_ids (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'salt_id int,' \
                            'drugbank_id nvarchar(255), ' \
                            '`primary` bool, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_salt_salt_drugbank_id FOREIGN KEY (salt_id)'\
                            'REFERENCES salts(id));'

        self.execute_query(drug_table_script)

    def create_synonyms(self):
        drug_table_script = 'CREATE TABLE synonyms (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'synonym nvarchar(255), ' \
                            'language nvarchar(255), ' \
                            'coder nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_synonym FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_products(self):
        drug_table_script = 'CREATE TABLE products (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'name nvarchar(1024), ' \
                            'labeller nvarchar(255), ' \
                            'ndc_id nvarchar(255), ' \
                            'ndc_product_code nvarchar(255), ' \
                            'dpd_id nvarchar(255), ' \
                            'ema_product_code nvarchar(255), ' \
                            'ema_ma_number nvarchar(255), ' \
                            'started_marketing_on nvarchar(255), ' \
                            'ended_marketing_on nvarchar(255), ' \
                            'dosage_form nvarchar(255), ' \
                            'strength nvarchar(255), ' \
                            'route nvarchar(255), ' \
                            'fda_application_number nvarchar(255), ' \
                            'generic bool, ' \
                            'over_the_counter bool, ' \
                            'approved bool, ' \
                            'country nvarchar(255), ' \
                            'source nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_product FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_international_brands(self):
        drug_table_script = 'CREATE TABLE international_brands (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'name nvarchar(1024), ' \
                            'company nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_international_brands FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_mixtures(self):
        drug_table_script = 'CREATE TABLE mixtures (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'name nvarchar(1024), ' \
                            'ingredients text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_mixture FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_packagers(self):
        drug_table_script = 'CREATE TABLE packagers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'name nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_packager FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_manufacturers(self):
        drug_table_script = 'CREATE TABLE manufacturers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'value nvarchar(255), ' \
                            'generic nvarchar(255), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_manufacturer FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_prices(self):
        drug_table_script = 'CREATE TABLE prices (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'description text, ' \
                            'cost decimal, ' \
                            'currency nvarchar(255), ' \
                            'unit nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_price FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_categories(self):
        drug_table_script = 'CREATE TABLE categories (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'category nvarchar(255), ' \
                            'mesh_id nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_category FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_affected_organisms(self):
        drug_table_script = 'CREATE TABLE affected_organisms (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_affected_organism FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_dosages(self):
        drug_table_script = 'CREATE TABLE dosages (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'form nvarchar(255), ' \
                            'route nvarchar(255), ' \
                            'strength nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_dosage FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_atc_codes(self):
        drug_table_script = 'CREATE TABLE atc_codes (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'code nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_atc_code FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_levels(self):
        drug_table_script = 'CREATE TABLE levels (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'atc_code_id int,' \
                            'code nvarchar(255), ' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_level FOREIGN KEY (atc_code_id)'\
                            'REFERENCES atc_codes(id));'

        self.execute_query(drug_table_script)

    def create_pdb_entries(self):
        drug_table_script = 'CREATE TABLE pdb_entries (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_pdb_entry FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_patents(self):
        drug_table_script = 'CREATE TABLE patents (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'number nvarchar(255), ' \
                            'country nvarchar(255), ' \
                            'approved datetime, ' \
                            'expires datetime, ' \
                            'pediatric_extension bool, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_patent FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_food_interactions(self):
        drug_table_script = 'CREATE TABLE food_interactions (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'value nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_food_interaction FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_drug_interactions(self):
        drug_table_script = 'CREATE TABLE drug_interactions (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'drugbank_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'description text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_drug_interaction FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_calculated_properties(self):
        drug_table_script = 'CREATE TABLE calculated_properties (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'kind nvarchar(255), ' \
                            'value text, ' \
                            'source nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_calculated_property FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_sequences(self):
        drug_table_script = 'CREATE TABLE sequences (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'value text, ' \
                            'format nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_sequence FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_experimental_properties(self):
        drug_table_script = 'CREATE TABLE experimental_properties (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'kind nvarchar(255), ' \
                            'value nvarchar(255), ' \
                            'source nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_experimental_property FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_external_identifiers(self):
        drug_table_script = 'CREATE TABLE external_identifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'resource nvarchar(1024), ' \
                            'identifier nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_external_identifier FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_external_links(self):
        drug_table_script = 'CREATE TABLE external_links (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'resource nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_external_link FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_pathways(self):
        drug_table_script = 'CREATE TABLE pathways (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'smpdb_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'category nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_pathway FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_pathway_drugs(self):
        drug_table_script = 'CREATE TABLE pathway_drugs (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'pathway_id int,' \
                            'drugbank_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_pathway_drug FOREIGN KEY (pathway_id)'\
                            'REFERENCES pathways(id));'

        self.execute_query(drug_table_script)

    def create_pathway_enzymes(self):
        drug_table_script = 'CREATE TABLE pathway_enzymes (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'pathway_id int,' \
                            'uniprot_id nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_pathway_enzyme FOREIGN KEY (pathway_id)'\
                            'REFERENCES pathways(id));'

        self.execute_query(drug_table_script)

    def create_reactions(self):
        drug_table_script = 'CREATE TABLE reactions (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'sequence nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_reaction FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_elements(self):
        drug_table_script = 'CREATE TABLE elements (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'reaction_id int,' \
                            'drugbank_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'side nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_reaction_element FOREIGN KEY (reaction_id)'\
                            'REFERENCES reactions(id));'

        self.execute_query(drug_table_script)

    def create_reaction_enzymes(self):
        drug_table_script = 'CREATE TABLE reaction_enzymes (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'reaction_id int,' \
                            'drugbank_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'uniprot_id nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_reaction_reaction_enzyme FOREIGN KEY (reaction_id)'\
                            'REFERENCES reactions(id));'

        self.execute_query(drug_table_script)

    def create_snp_effects(self):
        drug_table_script = 'CREATE TABLE snp_effects (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'protein_name nvarchar(1024), ' \
                            'gene_symbol nvarchar(255), ' \
                            'uniprot_id nvarchar(255), ' \
                            'rs_id nvarchar(255), ' \
                            'allele nvarchar(255), ' \
                            'defining_change nvarchar(255), ' \
                            'description text, ' \
                            'pubmed_id nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_snp_effect FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_snp_adverse_drug_reactions(self):
        drug_table_script = 'CREATE TABLE snp_adverse_drug_reactions (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'protein_name nvarchar(1024), ' \
                            'gene_symbol nvarchar(255), ' \
                            'uniprot_id nvarchar(255), ' \
                            'rs_id nvarchar(255), ' \
                            'allele nvarchar(255), ' \
                            'adverse_reaction nvarchar(255), ' \
                            'description text, ' \
                            'pubmed_id nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_snp_adverse_drug_reaction FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_targets(self):
        drug_table_script = 'CREATE TABLE targets (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'position int, ' \
                            'target_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'organism nvarchar(255), ' \
                            'known_action nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_target_actions(self):
        drug_table_script = 'CREATE TABLE target_actions (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_action FOREIGN KEY (target_id)'\
                            'REFERENCES targets(id));'

        self.execute_query(drug_table_script)

    def create_target_references_articles(self):
        drug_table_script = 'CREATE TABLE target_references_articles (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_id int,' \
                            'ref_id nvarchar(255), ' \
                            'pubmed_id nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_references_article FOREIGN KEY (target_id)'\
                            'REFERENCES targets(id));'

        self.execute_query(drug_table_script)

    def create_target_references_textbooks(self):
        drug_table_script = 'CREATE TABLE target_references_textbooks (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_id int,' \
                            'ref_id nvarchar(255), ' \
                            'isbn nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_references_textbook FOREIGN KEY (target_id)'\
                            'REFERENCES targets(id));'

        self.execute_query(drug_table_script)

    def create_target_references_links(self):
        drug_table_script = 'CREATE TABLE target_references_links (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_references_link FOREIGN KEY (target_id)'\
                            'REFERENCES targets(id));'

        self.execute_query(drug_table_script)

    def create_target_references_attachments(self):
        drug_table_script = 'CREATE TABLE target_references_attachments (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_references_attachment FOREIGN KEY (target_id)'\
                            'REFERENCES targets(id));'

        self.execute_query(drug_table_script)

    def create_target_polypeptides(self):
        drug_table_script = 'CREATE TABLE target_polypeptides (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_id int,' \
                            'polypeptide_id nvarchar(255), ' \
                            'source nvarchar(1024), ' \
                            'name nvarchar(1024), ' \
                            'general_function text, ' \
                            'specific_function text, ' \
                            'gene_name nvarchar(1024), ' \
                            'locus nvarchar(255), ' \
                            'cellular_location nvarchar(255), ' \
                            'transmembrane_regions nvarchar(255), ' \
                            'signal_regions nvarchar(255), ' \
                            'theoretical_pi decimal, ' \
                            'molecular_weight decimal, ' \
                            'chromosome_location nvarchar(255), ' \
                            'organism_ncbi_taxonomy_id int, ' \
                            'organism_ncbi_taxonomy_value nvarchar(255), ' \
                            'amino_acid_sequence_format nvarchar(255), ' \
                            'amino_acid_sequence_value text, ' \
                            'gene_sequence_format nvarchar(255), ' \
                            'gene_sequence_value text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_polypeptide FOREIGN KEY (target_id)'\
                            'REFERENCES targets(id));'

        self.execute_query(drug_table_script)

    def create_target_polypeptide_external_identifiers(self):
        drug_table_script = 'CREATE TABLE target_polypeptide_external_identifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_polypeptide_id int, ' \
                            'resource nvarchar(1024), ' \
                            'identifier nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_polypeptide_external_identifier FOREIGN KEY (target_polypeptide_id)'\
                            'REFERENCES target_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_target_polypeptide_synonyms(self):
        drug_table_script = 'CREATE TABLE target_polypeptide_synonyms (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_polypeptide_id int, ' \
                            'synonym nvarchar(255), ' \
                            'language nvarchar(255), ' \
                            'coder nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_polypeptide_synonym FOREIGN KEY (target_polypeptide_id)'\
                            'REFERENCES target_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_target_polypeptide_pfams(self):
        drug_table_script = 'CREATE TABLE target_polypeptide_pfams (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_polypeptide_id int, ' \
                            'identifier nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_polypeptide_pfam FOREIGN KEY (target_polypeptide_id)'\
                            'REFERENCES target_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_target_polypeptide_go_classifiers(self):
        drug_table_script = 'CREATE TABLE target_polypeptide_go_classifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'target_polypeptide_id int, ' \
                            'category nvarchar(255), ' \
                            'description text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_target_polypeptide_go_classifier FOREIGN KEY (target_polypeptide_id)'\
                            'REFERENCES target_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_enzymes(self):
        drug_table_script = 'CREATE TABLE enzymes (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'position int, ' \
                            'enzyme_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'organism nvarchar(255), ' \
                            'known_action nvarchar(255), ' \
                            'inhibition_strength nvarchar(255), ' \
                            'induction_strength nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_actions(self):
        drug_table_script = 'CREATE TABLE enzyme_actions (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_action FOREIGN KEY (enzyme_id)'\
                            'REFERENCES enzymes(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_references_articles(self):
        drug_table_script = 'CREATE TABLE enzyme_references_articles (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_id int,' \
                            'ref_id nvarchar(255), ' \
                            'pubmed_id nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_references_article FOREIGN KEY (enzyme_id)'\
                            'REFERENCES enzymes(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_references_textbooks(self):
        drug_table_script = 'CREATE TABLE enzyme_references_textbooks (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_id int,' \
                            'ref_id nvarchar(255), ' \
                            'isbn nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_references_textbook FOREIGN KEY (enzyme_id)'\
                            'REFERENCES enzymes(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_references_links(self):
        drug_table_script = 'CREATE TABLE enzyme_references_links (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_references_link FOREIGN KEY (enzyme_id)'\
                            'REFERENCES enzymes(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_references_attachments(self):
        drug_table_script = 'CREATE TABLE enzyme_references_attachments (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_references_attachment FOREIGN KEY (enzyme_id)'\
                            'REFERENCES enzymes(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_polypeptides(self):
        drug_table_script = 'CREATE TABLE enzyme_polypeptides (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_id int,' \
                            'polypeptide_id nvarchar(255), ' \
                            'source nvarchar(1024), ' \
                            'name nvarchar(1024), ' \
                            'general_function text, ' \
                            'specific_function text, ' \
                            'gene_name nvarchar(1024), ' \
                            'locus nvarchar(255), ' \
                            'cellular_location nvarchar(255), ' \
                            'transmembrane_regions nvarchar(255), ' \
                            'signal_regions nvarchar(255), ' \
                            'theoretical_pi decimal, ' \
                            'molecular_weight decimal, ' \
                            'chromosome_location nvarchar(255), ' \
                            'organism_ncbi_taxonomy_id int, ' \
                            'organism_ncbi_taxonomy_value nvarchar(255), ' \
                            'amino_acid_sequence_format nvarchar(255), ' \
                            'amino_acid_sequence_value text, ' \
                            'gene_sequence_format nvarchar(255), ' \
                            'gene_sequence_value text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_polypeptide FOREIGN KEY (enzyme_id)'\
                            'REFERENCES enzymes(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_polypeptide_external_identifiers(self):
        drug_table_script = 'CREATE TABLE enzyme_polypeptide_external_identifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_polypeptide_id int, ' \
                            'resource nvarchar(1024), ' \
                            'identifier nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_polypeptide_external_identifier FOREIGN KEY (enzyme_polypeptide_id)'\
                            'REFERENCES enzyme_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_polypeptide_synonyms(self):
        drug_table_script = 'CREATE TABLE enzyme_polypeptide_synonyms (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_polypeptide_id int, ' \
                            'synonym nvarchar(255), ' \
                            'language nvarchar(255), ' \
                            'coder nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_polypeptide_synonym FOREIGN KEY (enzyme_polypeptide_id)'\
                            'REFERENCES enzyme_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_polypeptide_pfams(self):
        drug_table_script = 'CREATE TABLE enzyme_polypeptide_pfams (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_polypeptide_id int, ' \
                            'identifier nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_polypeptide_pfam FOREIGN KEY (enzyme_polypeptide_id)'\
                            'REFERENCES enzyme_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_enzyme_polypeptide_go_classifiers(self):
        drug_table_script = 'CREATE TABLE enzyme_polypeptide_go_classifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'enzyme_polypeptide_id int, ' \
                            'category nvarchar(255), ' \
                            'description text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_enzyme_polypeptide_go_classifier FOREIGN KEY (enzyme_polypeptide_id)'\
                            'REFERENCES enzyme_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_carriers(self):
        drug_table_script = 'CREATE TABLE carriers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'position int, ' \
                            'carrier_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'organism nvarchar(255), ' \
                            'known_action nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_carrier_actions(self):
        drug_table_script = 'CREATE TABLE carrier_actions (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_action FOREIGN KEY (carrier_id)'\
                            'REFERENCES carriers(id));'

        self.execute_query(drug_table_script)

    def create_carrier_references_articles(self):
        drug_table_script = 'CREATE TABLE carrier_references_articles (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_id int,' \
                            'ref_id nvarchar(255), ' \
                            'pubmed_id nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_references_article FOREIGN KEY (carrier_id)'\
                            'REFERENCES carriers(id));'

        self.execute_query(drug_table_script)

    def create_carrier_references_textbooks(self):
        drug_table_script = 'CREATE TABLE carrier_references_textbooks (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_id int,' \
                            'ref_id nvarchar(255), ' \
                            'isbn nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_references_textbook FOREIGN KEY (carrier_id)'\
                            'REFERENCES carriers(id));'

        self.execute_query(drug_table_script)

    def create_carrier_references_links(self):
        drug_table_script = 'CREATE TABLE carrier_references_links (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_references_link FOREIGN KEY (carrier_id)'\
                            'REFERENCES carriers(id));'

        self.execute_query(drug_table_script)

    def create_carrier_references_attachments(self):
        drug_table_script = 'CREATE TABLE carrier_references_attachments (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_references_attachment FOREIGN KEY (carrier_id)'\
                            'REFERENCES carriers(id));'

        self.execute_query(drug_table_script)

    def create_carrier_polypeptides(self):
        drug_table_script = 'CREATE TABLE carrier_polypeptides (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_id int,' \
                            'polypeptide_id nvarchar(255), ' \
                            'source nvarchar(1024), ' \
                            'name nvarchar(1024), ' \
                            'general_function text, ' \
                            'specific_function text, ' \
                            'gene_name nvarchar(1024), ' \
                            'locus nvarchar(255), ' \
                            'cellular_location nvarchar(255), ' \
                            'transmembrane_regions nvarchar(255), ' \
                            'signal_regions nvarchar(255), ' \
                            'theoretical_pi decimal, ' \
                            'molecular_weight decimal, ' \
                            'chromosome_location nvarchar(255), ' \
                            'organism_ncbi_taxonomy_id int, ' \
                            'organism_ncbi_taxonomy_value nvarchar(255), ' \
                            'amino_acid_sequence_format nvarchar(255), ' \
                            'amino_acid_sequence_value text, ' \
                            'gene_sequence_format nvarchar(255), ' \
                            'gene_sequence_value text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_polypeptide FOREIGN KEY (carrier_id)'\
                            'REFERENCES carriers(id));'

        self.execute_query(drug_table_script)

    def create_carrier_polypeptide_external_identifiers(self):
        drug_table_script = 'CREATE TABLE carrier_polypeptide_external_identifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_polypeptide_id int, ' \
                            'resource nvarchar(1024), ' \
                            'identifier nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_polypeptide_external_identifier FOREIGN KEY (' \
                            'carrier_polypeptide_id)'\
                            'REFERENCES carrier_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_carrier_polypeptide_synonyms(self):
        drug_table_script = 'CREATE TABLE carrier_polypeptide_synonyms (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_polypeptide_id int, ' \
                            'synonym nvarchar(255), ' \
                            'language nvarchar(255), ' \
                            'coder nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_polypeptide_synonym FOREIGN KEY (carrier_polypeptide_id)'\
                            'REFERENCES carrier_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_carrier_polypeptide_pfams(self):
        drug_table_script = 'CREATE TABLE carrier_polypeptide_pfams (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_polypeptide_id int, ' \
                            'identifier nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_polypeptide_pfam FOREIGN KEY (carrier_polypeptide_id)'\
                            'REFERENCES carrier_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_carrier_polypeptide_go_classifiers(self):
        drug_table_script = 'CREATE TABLE carrier_polypeptide_go_classifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'carrier_polypeptide_id int, ' \
                            'category nvarchar(255), ' \
                            'description text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_carrier_polypeptide_go_classifier FOREIGN KEY (carrier_polypeptide_id)'\
                            'REFERENCES carrier_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_transporters(self):
        drug_table_script = 'CREATE TABLE transporters (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'drug_id int,' \
                            'position int, ' \
                            'transporter_id nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'organism nvarchar(255), ' \
                            'known_action nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter FOREIGN KEY (drug_id)'\
                            'REFERENCES drugs(id));'

        self.execute_query(drug_table_script)

    def create_transporter_actions(self):
        drug_table_script = 'CREATE TABLE transporter_actions (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_id int,' \
                            'value nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_action FOREIGN KEY (transporter_id)'\
                            'REFERENCES transporters(id));'

        self.execute_query(drug_table_script)

    def create_transporter_references_articles(self):
        drug_table_script = 'CREATE TABLE transporter_references_articles (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_id int,' \
                            'ref_id nvarchar(255), ' \
                            'pubmed_id nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_references_article FOREIGN KEY (transporter_id)'\
                            'REFERENCES transporters(id));'

        self.execute_query(drug_table_script)

    def create_transporter_references_textbooks(self):
        drug_table_script = 'CREATE TABLE transporter_references_textbooks (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_id int,' \
                            'ref_id nvarchar(255), ' \
                            'isbn nvarchar(255), ' \
                            'citation nvarchar(2048), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_references_textbook FOREIGN KEY (transporter_id)'\
                            'REFERENCES transporters(id));'

        self.execute_query(drug_table_script)

    def create_transporter_references_links(self):
        drug_table_script = 'CREATE TABLE transporter_references_links (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_references_link FOREIGN KEY (transporter_id)'\
                            'REFERENCES transporters(id));'

        self.execute_query(drug_table_script)

    def create_transporter_references_attachments(self):
        drug_table_script = 'CREATE TABLE transporter_references_attachments (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_id int,' \
                            'ref_id nvarchar(255), ' \
                            'title nvarchar(1024), ' \
                            'url nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_references_attachment FOREIGN KEY (transporter_id)'\
                            'REFERENCES transporters(id));'

        self.execute_query(drug_table_script)

    def create_transporter_polypeptides(self):
        drug_table_script = 'CREATE TABLE transporter_polypeptides (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_id int,' \
                            'polypeptide_id nvarchar(255), ' \
                            'source nvarchar(1024), ' \
                            'name nvarchar(1024), ' \
                            'general_function text, ' \
                            'specific_function text, ' \
                            'gene_name nvarchar(1024), ' \
                            'locus nvarchar(255), ' \
                            'cellular_location nvarchar(255), ' \
                            'transmembrane_regions nvarchar(255), ' \
                            'signal_regions nvarchar(255), ' \
                            'theoretical_pi decimal, ' \
                            'molecular_weight decimal, ' \
                            'chromosome_location nvarchar(255), ' \
                            'organism_ncbi_taxonomy_id int, ' \
                            'organism_ncbi_taxonomy_value nvarchar(255), ' \
                            'amino_acid_sequence_format nvarchar(255), ' \
                            'amino_acid_sequence_value text, ' \
                            'gene_sequence_format nvarchar(255), ' \
                            'gene_sequence_value text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_polypeptide FOREIGN KEY (transporter_id)'\
                            'REFERENCES transporters(id));'

        self.execute_query(drug_table_script)

    def create_transporter_polypeptide_external_identifiers(self):
        drug_table_script = 'CREATE TABLE transporter_polypeptide_external_identifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_polypeptide_id int, ' \
                            'resource nvarchar(1024), ' \
                            'identifier nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_polypeptide_external_identifier FOREIGN KEY (' \
                            'transporter_polypeptide_id)'\
                            'REFERENCES transporter_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_transporter_polypeptide_synonyms(self):
        drug_table_script = 'CREATE TABLE transporter_polypeptide_synonyms (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_polypeptide_id int, ' \
                            'synonym nvarchar(255), ' \
                            'language nvarchar(255), ' \
                            'coder nvarchar(255), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_polypeptide_synonym FOREIGN KEY (transporter_polypeptide_id)'\
                            'REFERENCES transporter_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_transporter_polypeptide_pfams(self):
        drug_table_script = 'CREATE TABLE transporter_polypeptide_pfams (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_polypeptide_id int, ' \
                            'identifier nvarchar(255), ' \
                            'name nvarchar(1024), ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_polypeptide_pfam FOREIGN KEY (transporter_polypeptide_id)'\
                            'REFERENCES transporter_polypeptides(id));'

        self.execute_query(drug_table_script)

    def create_transporter_polypeptide_go_classifiers(self):
        drug_table_script = 'CREATE TABLE transporter_polypeptide_go_classifiers (' \
                            'id int NOT NULL AUTO_INCREMENT,' \
                            'transporter_polypeptide_id int, ' \
                            'category nvarchar(255), ' \
                            'description text, ' \
                            'PRIMARY KEY (`id`),'\
                            'CONSTRAINT fk_drug_transporter_polypeptide_go_classifier FOREIGN KEY (' \
                            'transporter_polypeptide_id)'\
                            'REFERENCES transporter_polypeptides(id));'

        self.execute_query(drug_table_script)
