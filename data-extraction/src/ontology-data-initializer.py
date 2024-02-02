import os
import uuid

from pyfuseki import FusekiQuery, FusekiUpdate
from rdflib import Graph, Namespace, URIRef, Literal

from src import utils
from src.logger import LOGGER
from src.sparql_queries import insert_esolang_multiple_query, insert_typing_discipline_query, \
    insert_computer_language_query, insert_developer_query, insert_programming_paradigm_query, insert_country_query, \
    query_check_existence


def insert(sparql_query):
    g = Graph()
    ela = Namespace("http://www.semanticweb.org/ontologies/ELA#")
    g.update(sparql_query)
    fuseki = FusekiUpdate('http://localhost:3030', 'ELA')
    try:
        fuseki.insert_graph(g)
    except Exception as e:
        LOGGER.error(str(e))


def exists(label):
    query_check_existence_f = query_check_existence.format(label=label)
    fuseki_query = FusekiQuery('http://localhost:3030', 'ELA')
    status = fuseki_query.run_sparql(query_check_existence_f).convert()['boolean']
    return status


def get_all_esolangs(sparql_query):
    fuseki_query = FusekiQuery('http://localhost:3030', 'ELA')
    query_result = fuseki_query.run_sparql(sparql_query)
    data = query_result.convert()['results']['bindings']
    return format_data(data)


def format_data(data):
    # Create an RDF graph to store the retrieved data
    g = Graph()
    for entry in data:
        # Add triples to the graph based on the retrieved data
        # (assuming the structure of your data, adjust as needed)
        g.add((URIRef(entry['subject']['value']),
               URIRef(entry['property']['value']),
               Literal(entry['value']['value'])))

    # Get the N3 serialization of the retrieved RDF data
    serialized_data = g.n3()

    return data


def format_prop(esolang_props, dict_key, prop_key, onto_key, datatype, dot=False, prefix='ela', data_prop=True, ):
    property_values = ''
    if esolang_props.get(prop_key):
        if type(esolang_props[prop_key]) != str:
            for value in esolang_props[prop_key]:
                if data_prop:
                    property_values += f'       {prefix}:{onto_key} "{value}"{datatype} ;\n'
                else:
                    property_values += f'       {prefix}:{onto_key} {prefix}:{value.replace(" ", "_")} ;\n'
        else:
            if data_prop:
                property_values = f'       {prefix}:{onto_key} "{esolang_props[prop_key]}"{datatype} ;\n'
            else:
                property_values = f'       {prefix}:{onto_key} {prefix}:{esolang_props[prop_key].replace(" ", "_")} ;\n'
    if dot:
        property_values = property_values[:-2] + '.'
    return property_values

    #

    #


def generate_unique_id():
    unique_id = str(uuid.uuid4())
    return unique_id


def insert_tp_discipline(values):
    if type(values) == str:
        insert_typing_discipline_query_f = insert_typing_discipline_query.format(
            individual_id=generate_unique_id(),
            label=values
        )
        try:
            if not exists(values):
                insert(insert_typing_discipline_query_f)
        except:
            LOGGER.warning(f"Failed for {values}")
            LOGGER.info(insert_typing_discipline_query_f)
    else:
        for td in values:
            insert_typing_discipline_query_f = insert_typing_discipline_query.format(
                individual_id=generate_unique_id(),
                label=td
            )
            try:
                if not exists(td):
                    insert(insert_typing_discipline_query_f)
            except:
                LOGGER.warning(f"Failed for {td}")
                LOGGER.info(insert_typing_discipline_query_f)


def insert_pr_paradigm(values):
    if type(values) == str:
        insert_programming_paradigm_query_f = insert_programming_paradigm_query.format(
            individual_id=generate_unique_id(),
            label=values
        )

        try:
            if not exists(values):
                insert(insert_programming_paradigm_query_f)
        except:
            LOGGER.warning(f"Failed for {values}")
            LOGGER.info(insert_programming_paradigm_query_f)
    else:
        for pp in values:
            insert_programming_paradigm_query_f = insert_programming_paradigm_query.format(
                individual_id=generate_unique_id(),
                label=pp
            )
            try:
                if not exists(pp):
                    insert(insert_programming_paradigm_query_f)
            except:
                LOGGER.warning(f"Failed for {pp}")
                LOGGER.info(insert_programming_paradigm_query_f)


def insert_countries(values):
    if type(values) == str:
        insert_country_query_f = insert_country_query.format(
            individual_id=generate_unique_id(),
            label=values
        )
        try:
            if not exists(values):
                insert(insert_country_query_f)
        except:
            LOGGER.warning(f"Failed for {values}")
            LOGGER.info(insert_country_query_f)
    else:
        for c in values:
            insert_country_query_f = insert_country_query.format(
                individual_id=generate_unique_id(),
                label=c
            )
            try:
                if not exists(c):
                    insert(insert_country_query_f)
            except:
                LOGGER.warning(f"Failed for {c}")
                LOGGER.info(insert_country_query_f)


def insert_developers(values):
    if type(values) == str:
        insert_developer_query_f = insert_developer_query.format(
            individual_id=generate_unique_id(),
            label=values
        )
        try:

            insert(insert_developer_query_f)
        except:
            LOGGER.warning(f"Failed for {values}")
            LOGGER.info(insert_developer_query_f)
    else:
        for dev in values:
            insert_developer_query_f = insert_developer_query.format(
                individual_id=generate_unique_id(),
                label=dev
            )
            try:

                insert(insert_developer_query_f)
            except:
                LOGGER.warning(f"Failed for {dev}")
                LOGGER.info(insert_developer_query_f)


def insert_computer_languages(values):
    if type(values) == str:
        insert_computer_language_query_f = insert_computer_language_query.format(
            individual_id=generate_unique_id(),
            label=values
        )
        try:

            insert(insert_computer_language_query_f)
        except:
            LOGGER.warning(f"Failed for {values}")
            LOGGER.info(insert_computer_language_query_f)
    else:
        for cl in values:
            insert_computer_language_query_f = insert_computer_language_query.format(
                individual_id=generate_unique_id(),
                label=cl
            )
            try:

                insert(insert_computer_language_query_f)
            except:
                LOGGER.warning(f"Failed for {cl}")
                LOGGER.info(insert_computer_language_query_f)


def main():
    #
    # # Replace the placeholder values
    # insert_esolang_query_f = insert_esolang_query.format(
    #     individual_id="exampleEsolang",
    #     description="Description of the example esolang",
    #     version="1.0",
    #     freebase_id="exampleFreebaseID",
    #     github_topic="exampleGitHubTopic",
    #     knowledge_graph_id="exampleKnowledgeGraphID",
    #     mime_type="exampleMIMEType",
    #     microsoft_academic_id="exampleMicrosoftAcademicID",
    #     quora_topic_id="exampleQuoraTopicID",
    #     stack_exchange_tag="exampleStackExchangeTag",
    #     creation_date="2022-02-01",
    #     source="exampleSource",
    #     discoverer_inventor="exampleDiscovererInventor",
    #     file_extension="exampleFileExtension",
    #     icon_url="exampleIconURL",
    #     image_url="exampleImageURL",
    #     named_after="exampleNamedAfter",
    #     official_website_url="exampleOfficialWebsiteURL",
    #     subreddit="exampleSubreddit",
    #     label="Example Esolang",
    #     alt_label="ExampleAltLabel",
    #     country_id="exampleCountry2",
    #     developer_id="exampleDeveloper",
    #     computer_language_id="exampleComputerLanguage",
    #     programming_paradigm_id="exampleProgrammingParadigm",
    #     typing_discipline_id="exampleTypingDiscipline",
    # )
    #
    # insert(insert_country_query_f)
    # insert(insert_developer_query_f)
    # insert(insert_computer_language_query_f)
    # insert(insert_programming_paradigm_query_f)
    # insert(insert_typing_discipline_query_f)
    # insert(insert_esolang_query_f)

    # print(get_all_esolangs(sparql_query_get_all_esolangs))

    files = os.listdir('output/wikidata/updated')
    for file in files:
        filepath = os.path.join(os.path.join(os.getcwd(), 'output\\wikidata\\updated'), file)
        # print(filepath)
        props = utils.extract_properties(filepath)
        utils.write_json_file(os.path.join(os.path.join(os.getcwd(), 'output\\wikidata\\properties'), file),
                              props[0])
        esolang = props[0]
        esolang_id = esolang['Language']
        property_values = {
            "country": "",
            "developer": "",
            "computer_language": "",
            "programming_paradigm": "",
            "typing_discipline": "",
            "knowledge_graph": "",
            "microsoft_academic": "",
            "quora_topic": "",
            "stack_exchange_tag": "",
            "creation_date": "",
            "freebase": "",
            "github_topic": "",
            "mime_type": "",
            "file_extension": "",
            "icon_url": "",
            "image_url": "",
            "official_website_url": "",
            "subreddit": "",
            "label": "",
            "altLabel": "",
            "version": "",
            "designed_by": ""

        }

        esolang_props = esolang['Properties']

        if esolang_props.get('http://www.wikidata.org/prop/direct/country'):
            insert_countries(esolang_props['http://www.wikidata.org/prop/direct/country'])
        if esolang_props.get('http://www.wikidata.org/prop/direct/developer'):
            insert_developers(esolang_props['http://www.wikidata.org/prop/direct/developer'])
        if esolang_props.get('http://www.wikidata.org/prop/direct/dialect of computer language'):
            insert_computer_languages(esolang_props['http://www.wikidata.org/prop/direct/dialect of computer language'])
        if esolang_props.get('http://www.wikidata.org/prop/direct/programming paradigm'):
            insert_pr_paradigm(esolang_props['http://www.wikidata.org/prop/direct/programming paradigm'])
        if esolang_props.get('http://www.wikidata.org/prop/direct/typing discipline'):
            insert_tp_discipline(esolang_props['http://www.wikidata.org/prop/direct/typing discipline'])

        # Object properties

        property_values['country'] = format_prop(esolang_props, 'country',
                                                 'http://www.wikidata.org/prop/direct/country', 'country', '',
                                                 data_prop=False)

        property_values['designed_by'] = format_prop(esolang_props, 'designed_by',
                                                     'http://www.wikidata.org/prop/designed by', 'designed_by', '',
                                                     data_prop=False)

        property_values['developer'] = format_prop(esolang_props, 'developer',
                                                   'http://www.wikidata.org/prop/direct/developer', 'developer', '',
                                                   data_prop=False)
        property_values['dialect_of_computer_language'] = format_prop(esolang_props, 'dialect_of_computer_language',
                                                                      'http://www.wikidata.org/prop/direct/dialect of computer language',
                                                                      'dialect_of_computer_language',
                                                                      '', data_prop=False)
        property_values['influenced_by'] = format_prop(esolang_props, 'influenced_by',
                                                       'http://www.wikidata.org/prop/direct/influenced by',
                                                       'influenced_by', '',
                                                       data_prop=False)
        property_values['instance_of'] = format_prop(esolang_props, 'instance_of',
                                                     'http://www.wikidata.org/prop/direct/instance of', 'instance_of',
                                                     '',
                                                     data_prop=False)
        property_values['programming_paradigm'] = format_prop(esolang_props, 'programming_paradigm',
                                                              'http://www.wikidata.org/prop/direct/programming paradigm',
                                                              'programming_paradigm',
                                                              '', data_prop=False)
        property_values['typing_discipline'] = format_prop(esolang_props, 'typing_discipline',
                                                           'http://www.wikidata.org/prop/direct/typing discipline',
                                                           'typing_discipline', '',
                                                           data_prop=False)

        # Data Properties
        property_values['version'] = format_prop(esolang_props, 'version', 'http://schema.org/version', 'version',
                                                 '^^xsd:string')

        property_values['knowledge_graph'] = format_prop(esolang_props, 'knowledge_graph',
                                                         'http://www.wikidata.org/prop/direct/Google Knowledge Graph ID',
                                                         'Google_Knowledge_Graph_ID',
                                                         '^^xsd:string')
        property_values['microsoft_academic'] = format_prop(esolang_props, 'microsoft_academic',
                                                            'http://www.wikidata.org/prop/direct/Microsoft Academic ID',
                                                            'Microsoft_Academic_ID',
                                                            '^^xsd:string')
        property_values['quora_topic'] = format_prop(esolang_props, 'quora_topic',
                                                     'http://www.wikidata.org/prop/direct/Quora topic ID',
                                                     'Quora_topic_ID',
                                                     '^^xsd:string')
        property_values['stack_exchange_tag'] = format_prop(esolang_props, 'stack_exchange_tag',
                                                            'http://www.wikidata.org/prop/direct/Stack Exchange tag',
                                                            'Stack_Exchange_tag',
                                                            '^^xsd:string')
        property_values['creation_date'] = format_prop(esolang_props, 'creation_date',
                                                       'http://www.wikidata.org/prop/direct/inception', 'creation',
                                                       '^^xsd:date')
        property_values['freebase'] = format_prop(esolang_props, 'freebase',
                                                  'http://www.wikidata.org/prop/direct/Freebase ID', 'Freebase_ID',
                                                  '^^xsd:string')
        property_values['github_topic'] = format_prop(esolang_props, 'github_topic',
                                                      'http://www.wikidata.org/prop/direct/GitHub topic',
                                                      'GitHub_topic',
                                                      '^^xsd:string')
        property_values['mime_type'] = format_prop(esolang_props, 'mime_type',
                                                   'http://www.wikidata.org/prop/direct/MIME type', 'MIME_type',
                                                   '^^xsd:anyURI')
        property_values['file_extension'] = format_prop(esolang_props, 'file_extension',
                                                        'http://www.wikidata.org/prop/direct/file extension',
                                                        'file_extension',
                                                        '^^xsd:string')
        property_values['icon_url'] = format_prop(esolang_props, 'icon_url',
                                                  'http://www.wikidata.org/prop/direct/icon', 'icon',
                                                  '^^xsd:anyURI')
        property_values['image_url'] = format_prop(esolang_props, 'image_url',
                                                   'http://www.wikidata.org/prop/direct/image', 'image',
                                                   '^^xsd:anyURI')
        property_values['official_website_url'] = format_prop(esolang_props, 'official_website_url',
                                                              'http://www.wikidata.org/prop/direct/official website',
                                                              'official_website',
                                                              '^^xsd:anyURI')
        property_values['subreddit'] = format_prop(esolang_props, 'subreddit',
                                                   'http://www.wikidata.org/prop/direct/subreddit', 'subreddit',
                                                   '^^xsd:anyURI')
        property_values['label'] = format_prop(esolang_props, 'label',
                                               'http://www.w3.org/2000/01/rdf-schema#label', 'label',
                                               '^^xsd:string', prefix='rdfs')
        property_values['altLabel'] = format_prop(esolang_props, 'altLabel',
                                                  'http://www.w3.org/2004/02/skos/core#altLabel', 'altLabel',
                                                  '^^xsd:string', prefix='skos')
        insert_esolang_multiple_query_f = insert_esolang_multiple_query.format(
            individual_id=esolang_id.replace('http://www.wikidata.org/entity/', ''),
            country=property_values["country"],
            developer=property_values["developer"],
            computer_language=property_values["computer_language"],
            programming_paradigm=property_values["programming_paradigm"],
            typing_discipline=property_values["typing_discipline"],
            knowledge_graph=property_values["knowledge_graph"],
            version=property_values["version"],
            microsoft_academic=property_values["microsoft_academic"],
            quora_topic=property_values["quora_topic"],
            stack_exchange_tag=property_values["stack_exchange_tag"],
            creation_date=property_values["creation_date"],
            freebase=property_values["freebase"],
            github_topic=property_values["github_topic"],
            mime_type=property_values["mime_type"],
            file_extension=property_values["file_extension"],
            icon_url=property_values["icon_url"],
            image_url=property_values["image_url"],
            official_website_url=property_values["official_website_url"],
            subreddit=property_values["subreddit"],
            label=property_values["label"],
            alt_label=property_values["altLabel"],
            designed_by=property_values["designed_by"]
        ).replace('   ', ' ').replace('   ', ' ').replace('   ', ' ') \
            .replace('  ', ' ').replace('  ', ' ').replace('  ', ' ') \
            .replace('\n \n', '\n').replace('\n \n', '\n').replace('\n \n', '\n') \
            .replace('\n\n\n', '\n').replace('\n\n\n', '\n').replace('\n\n\n', '\n') \
            .replace('\n\n', '\n').replace('\n\n', '\n').replace('\n\n', '\n') \
            .replace(';\n .', '.')

        try:
            insert(insert_esolang_multiple_query_f)
        except:
            LOGGER.warning(f"Failed for {file}")
            LOGGER.info(insert_esolang_multiple_query_f)


if __name__ == "__main__":
    main()
