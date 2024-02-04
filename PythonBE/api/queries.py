RDF_STORE_URL = "http://localhost:3030"
RDF_STORE_DATASET_NAME = "ELA"

insert_esolang_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT DATA {
  ela:{individual_id} rdf:type ela:esolang ;
                      ela:country ela:{country} ;
                      ela:designed_by ela:{designed_by} ;
                      ela:developer ela:{developer} ;
                      ela:dialect_of_computer_language ela:{dialect_of_computer_language} ;
                      ela:influenced_by ela:{influenced_by} ;
                      ela:instance_of ela:{instance_of} ;
                      ela:programming_paradigm ela:{programming_paradigm} ;
                      ela:typing_discipline ela:{typing_discipline} .
  ela:{individual_id} 
                      ela:Google_Knowledge_Graph_ID "{Microsoft_Academic_ID}"^^xsd:string ;
                      ela:version "{version}"^^xsd:string ;
                      ela:Microsoft_Academic_ID "{Microsoft_Academic_ID}"^^xsd:string ;
                      ela:Quora_topic_ID "{Quora_topic_ID}"^^xsd:string ;
                      ela:Stack_Exchange_tag "{Stack_Exchange_tag}"^^xsd:string ;
                      ela:creation "{creation}"^^xsd:date ;
                      ela:Freebase_ID "{Freebase_ID}"^^xsd:string ;
                      ela:GitHub_topic "{GitHub_topic}"^^xsd:string ;
                      ela:MIME_type "{MIME_type}"^^xsd:string ;
                      ela:file_extension "{file_extension}"^^xsd:string ;
                      ela:icon "{icon}"^^xsd:anyURI ;
                      ela:image "{image}"^^xsd:anyURI ;
                      ela:official_website "{official_website}"^^xsd:anyURI ;
                      ela:subreddit "{subreddit}"^^xsd:anyURI ;
                      rdfs:label "{label}"^^xsd:string ;
                      skos:altLabel "{altLabel}"^^xsd:string .
}
"""

esolangs_labels_filtered = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?subject ?label
WHERE {{
  ?subject rdf:type ela:esolang.
  ?subject rdfs:label ?label.
  
  {programming_paradigm}
  {influenced_by}
  {typing_discipline}
  {official_website}
}}

"""
esolangs_labels_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>

SELECT ?subject ?label
WHERE {
  ?subject rdf:type ela:esolang.
  ?subject rdfs:label ?label.
}
"""

pp_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>

SELECT ?subject ?label
WHERE {
  ?subject rdf:type ela:programming_paradigm.
  ?subject rdfs:label ?label.
}
"""

cl_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>

SELECT ?subject ?label
WHERE {
  ?subject rdf:type ela:computer_language.
  ?subject rdfs:label ?label.
}
"""

country_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>

SELECT ?subject ?label
WHERE {
  ?subject rdf:type ela:country.
  ?subject rdfs:label ?label.
}
"""

typing_discipline_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>

SELECT ?subject ?label
WHERE {
  ?subject rdf:type ela:typing_discipline.
  ?subject rdfs:label ?label.
}
"""

esolang_data_query = """
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>

SELECT ?predicate ?object
WHERE {{
  ela:{value} ?predicate ?object .
}}
"""

RDF_SIMPLE_QUERIES = {
    'esolangs_labels': esolangs_labels_query,
    'programming_paradigms': pp_query,
    'computer_language': cl_query,
    'country': country_query,
    'typing_discipline': typing_discipline_query,
    'esolang_data': esolang_data_query,
}
RDF_COMPLEX_QUERIES = {
    'esolang_data': esolang_data_query,
}
