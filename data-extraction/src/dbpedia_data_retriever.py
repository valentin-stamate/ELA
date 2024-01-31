import json
import time

import requests

from src.logger import LOGGER
from src.utils import read_json_file, write_file


def execute_sparql_query(query):
    LOGGER.info("Executing query")
    #LOGGER.info(query)
    endpoint_url = "https://dbpedia.org/sparql"
    params = {
        'format': 'json',
        'query': query
    }

    response = requests.get(endpoint_url, params=params)
    data = response.json()
    # LOGGER.info('Query response')
    #LOGGER.info(data)

    return data


def generate_sparql_query(language_title):
    sparql_query = f"""
        PREFIX dbo: <http://dbpedia.org/ontology/>
        rPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        
        SELECT ?language ?property ?value
        WHERE {{
          ?language a dbo:Language ;
                     rdfs:label "{language_title}"@en ;
                     ?property ?value .
        }}
    """

    return sparql_query


def create_json_object(properties_dict):
    result_list = []

    for language, properties in properties_dict.items():
        language_data = {"Language": language, "Properties": []}

        for property_name, values in properties.items():
            property_data = {"Property": property_name, "Values": list(values)}
            language_data["Properties"].append(property_data)

        result_list.append(language_data)

    return json.dumps(result_list, indent=2)


def print_results(results, title):
    # Dictionary to store unique properties and their sets of values
    properties_dict = {}
    # language = ''
    # Extract properties and values from the result
    for binding in results['results']['bindings']:
        language = binding.get('language', {}).get('value', 'N/A')
        property_name = binding.get('property', {}).get('value', 'N/A')
        value = binding.get('value', {}).get('value', 'N/A')

        # Aggregate properties and values in the dictionary
        if language not in properties_dict:
            properties_dict[language] = {}

        if property_name not in properties_dict[language]:
            properties_dict[language][property_name] = set()

        properties_dict[language][property_name].add(value)

    # Print the aggregated results
    for language, properties in properties_dict.items():
        print(f"Language: {language}")
        for property_name, values in properties.items():
            print(f"Property: {property_name}")
            print(f"Values: {', '.join(values)}")
        print("------")

    # Create and print the JSON object
    # if language != '':
    json_object = create_json_object(properties_dict)
    write_file(f"src/output/dbpedia/{title}.json", json_object)


def get_data():
    language_list = read_json_file('src/output/languages.json')
    for item in language_list:
        try:
            data = execute_sparql_query(generate_sparql_query(item['title']))
            print_results(data, item['title'])
            time.sleep(0.2)
        except Exception as e:
            pass
            # LOGGER.error(str(e))
