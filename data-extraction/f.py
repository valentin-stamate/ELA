props = [
    'http://www.wikidata.org/prop/direct/described by source',
    'http://schema.org/version',
    'http://www.wikidata.org/prop/direct/Microsoft Academic ID',
    'http://www.wikidata.org/prop/direct/Quora topic ID',
    'http://www.wikidata.org/prop/direct/designed by',
    'http://www.wikidata.org/prop/direct/influenced by',
    'http://www.wikidata.org/prop/direct/programming paradigm',
    'http://www.wikidata.org/prop/direct/file extension',
    'http://www.wikidata.org/prop/direct/named after',
    'http://www.wikidata.org/prop/direct/GitHub topic',
    'http://www.wikidata.org/prop/direct/Google Knowledge Graph ID',
    'http://www.wikidata.org/prop/direct/MIME type',
    'http://www.wikidata.org/prop/direct/instance of',
    'http://www.wikidata.org/prop/direct/Stack Exchange tag',
    'http://www.wikidata.org/prop/direct/developer',
    'http://www.w3.org/2000/01/rdf-schema#label',
    'http://www.wikidata.org/prop/direct/typing discipline',
    'http://www.wikidata.org/prop/direct/inception',
    'http://www.wikidata.org/prop/direct/Freebase ID',
    'http://www.wikidata.org/prop/direct/dialect of computer language',
    'http://www.wikidata.org/prop/direct/subreddit',
    'http://www.wikidata.org/prop/direct/icon',
    'http://www.wikidata.org/prop/direct/discoverer or inventor',
    'http://www.wikidata.org/prop/direct/official website',
    'http://www.wikidata.org/prop/direct/country',
    'http://www.w3.org/2004/02/skos/core#altLabel',
    'http://www.wikidata.org/prop/direct/image'
]

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

q="""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
INSERT DATA {
 ela:Q2072087 rdf:type ela:esolang ;
 ela:programming_paradigm ela:imperative_programming ;
 ela:programming_paradigm ela:structured_programming .
 ela:Q2072087 
 ela:version "1729773891"^^xsd:string ;
 ela:creation "1964-01-01T00:00:00Z"^^xsd:date ;
 ela:Freebase_ID "/m/06ypf2"^^xsd:string ;
 rdfs:label "P′′"^^xsd:string ;
 skos:altLabel "P prime prime"^^xsd:string ;
 skos:altLabel "P''"^^xsd:string .
}
"""
insert(q)