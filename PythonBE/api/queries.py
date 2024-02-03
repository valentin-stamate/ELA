RDF_STORE_URL = "http://localhost:3030"
RDF_STORE_DATASET_NAME = "ELA"

esolangs_labels_filtered="""
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
