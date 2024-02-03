insert_typing_discipline_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT DATA {{
  ela:{individual_id} rdf:type ela:typing_discipline ;
                     rdfs:label "{label}" .
}}
"""


# Execute the query


insert_programming_paradigm_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

INSERT DATA {{
  ela:{individual_id} rdf:type ela:programming_paradigm ;
                    rdfs:label "{label}" .
}}
"""

# Execute the query

insert_computer_language_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT DATA {{
  ela:{individual_id} rdf:type ela:computer_language ;
                    rdfs:label "{label}" .
}}
"""

insert_developer_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT DATA {{
  ela:{individual_id} rdf:type ela:developer ;
                      rdfs:label "{label}" .
}}
"""

# Execute the query
insert_country_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT DATA {{
  ela:{individual_id} rdf:type ela:country ;
                    rdfs:label "{label}" .
}}
"""

# Execute the query

# Replace placeholder values with actual data
insert_esolang_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT DATA {{
  ela:{individual_id} rdf:type ela:esolang ;
                      ela:country ela:{country_id} ;
                      ela:designed_by ela:{developer_id} ;
                      ela:developer ela:{developer_id} ;
                      ela:dialect_of_computer_language ela:{computer_language_id} ;
                      ela:influenced_by ela:{computer_language_id} ;
                      ela:instance_of ela:{computer_language_id} ;
                      ela:programming_paradigm ela:{programming_paradigm_id} ;
                      ela:typing_discipline ela:{typing_discipline_id} .
                      
  ela:{individual_id} ela:Google_Knowledge_Graph_ID "{knowledge_graph_id}"^^xsd:string ;
                      ela:version "{version}"^^xsd:string ;
                      ela:Microsoft_Academic_ID "{microsoft_academic_id}"^^xsd:string ;
                      ela:Quora_topic_ID "{quora_topic_id}"^^xsd:string ;
                      ela:Stack_Exchange_tag "{stack_exchange_tag}"^^xsd:string ;
                      ela:creation "{creation_date}"^^xsd:date ;
                      ela:Freebase_ID "{freebase_id}"^^xsd:string ;
                      ela:GitHub_topic "{github_topic}"^^xsd:string ;
                      ela:MIME_type "{mime_type}"^^xsd:string ;
                      ela:file_extension "{file_extension}"^^xsd:string ;
                      ela:icon "{icon_url}"^^xsd:anyURI ;
                      ela:image "{image_url}"^^xsd:anyURI ;
                      ela:official_website "{official_website_url}"^^xsd:anyURI ;
                      ela:subreddit "{subreddit}"^^xsd:anyURI ;
                      rdfs:label "{label}"^^xsd:string ;
                      skos:altLabel "{alt_label}"^^xsd:string .
}}
"""

insert_esolang_multiple_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT DATA {{
  ela:{individual_id} rdf:type ela:esolang ;
                      {country} 
                      {developer} 
                      {computer_language} 
                      {programming_paradigm} 
                      {influenced_by}
                      {typing_discipline} .

  ela:{individual_id} {knowledge_graph}
                      {version}
                      {microsoft_academic}
                      {quora_topic}
                      {stack_exchange_tag}
                      {creation_date}
                      {freebase}
                      {github_topic}
                      {mime_type}
                      {file_extension}
                      {icon_url}
                      {image_url}
                      {official_website_url}
                      {subreddit}
                      {label}
                      {alt_label} .
}}
"""

sparql_query_get_all_esolangs = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?subject
WHERE {
  ?subject rdf:type ela:esolang.
}
"""




# insert_typing_discipline_query = insert_typing_discipline_query.format(
#     individual_id="exampleTypingDiscipline",
#     label="Example Typing Discipline"
# )
#
# insert_programming_paradigm_query = insert_programming_paradigm_query.format(
#     individual_id="exampleProgrammingParadigm",
#     label="Example Programming Paradigm"
# )
#
# insert_computer_language_query = insert_computer_language_query.format(
#     individual_id="exampleComputerLanguage",
#     label="Example Computer Language"
# )
#
# insert_developer_query = insert_developer_query.format(
#     individual_id="exampleDeveloper",
#     label="Example Developer"
# )
#
# insert_country_query = insert_country_query.format(
#     individual_id="exampleCountry",
#     label="Example Country"
# )
# # Replace the placeholder values
# insert_esolang_query = insert_esolang_query.format(
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
#     creation_date="exampleCreationDate",
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
#     country_id="exampleCountry",
#     developer_id="exampleDeveloper",
#     computer_language_id="exampleComputerLanguage",
#     programming_paradigm_id="exampleProgrammingParadigm",
#     typing_discipline_id="exampleTypingDiscipline"
# )

# Execute the query
query_check_existence = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

ASK WHERE {{
  ?existing_pp rdfs:label "{label}" .
}}
"""