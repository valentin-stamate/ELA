from pyfuseki import FusekiQuery

from api.queries import *


# =================================================== DATA FUNCTIONS ===================================================
def insert(data):
    pass


def get_data(key):
    if RDF_SIMPLE_QUERIES.get(key) is None:
        raise KeyError()
    fuseki_query = FusekiQuery(RDF_STORE_URL, RDF_STORE_DATASET_NAME)
    query_result = fuseki_query.run_sparql(RDF_SIMPLE_QUERIES[key])
    data = query_result.convert()['results']['bindings']
    return FORMAT_FUNCTIONS[key](data)


def get_specific_data(key, value):
    if RDF_COMPLEX_QUERIES.get(key) is None:
        raise KeyError()
    formatted_query = RDF_COMPLEX_QUERIES[key].format(value=value)
    print(formatted_query)
    fuseki_query = FusekiQuery(RDF_STORE_URL, RDF_STORE_DATASET_NAME)
    query_result = fuseki_query.run_sparql(formatted_query)
    data = query_result.convert()['results']['bindings']
    return FORMAT_FUNCTIONS[key](data)


# ================================================== FORMAT FUNCTIONS ==================================================

def format_esolangs_results(results):
    formatted_results = []
    for result in results:
        subject = result.get("subject", {}).get("value", None)
        label = result.get("label", {}).get("value", None)

        if subject and label:
            formatted_results.append({"esolang": subject, "label": label})

    return formatted_results


def format_pp_results(results):
    formatted_results = []
    for result in results:
        subject = result.get("subject", {}).get("value", None)
        label = result.get("label", {}).get("value", None)

        if subject and label:
            formatted_results.append({"programming_paradigm": subject, "label": label})

    return formatted_results


def format_computer_language_results(results):
    formatted_results = []
    for result in results:
        subject = result.get("subject", {}).get("value", None)
        label = result.get("label", {}).get("value", None)

        if subject and label:
            formatted_results.append({"computer_language": subject, "label": label})

    return formatted_results


def format_country_results(results):
    formatted_results = []
    for result in results:
        subject = result.get("subject", {}).get("value", None)
        label = result.get("label", {}).get("value", None)

        if subject and label:
            formatted_results.append({"country": subject, "label": label})

    return formatted_results


def format_typing_discipline_results(results):
    formatted_results = []
    for result in results:
        subject = result.get("subject", {}).get("value", None)
        label = result.get("label", {}).get("value", None)

        if subject and label:
            formatted_results.append({"typing_discipline": subject, "label": label})

    return formatted_results


def format_esolang_data_results(results):
    formatted_results = []
    for result in results:
        subject = result.get("predicate", {}).get("value", None)
        label = result.get("object", {}).get("value", None)

        if subject and label:
            formatted_results.append({"property": subject.split('#')[1], "value": label})

    return formatted_results


FORMAT_FUNCTIONS = {
    'esolangs_labels': format_esolangs_results,
    'programming_paradigms': format_pp_results,
    'computer_language': format_computer_language_results,
    'country': format_country_results,
    'typing_discipline': format_typing_discipline_results,
    'esolang_data': format_esolang_data_results
}
