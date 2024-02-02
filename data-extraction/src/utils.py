import json

import requests

from src import conf
from src.logger import LOGGER


def write_json_file(file_path: str, data):
    # Path to the JSON file
    LOGGER.info(f"Writing file {file_path}")
    # Write the extracted list to a JSON file
    with open(file_path, 'w+') as json_file:
        json.dump(data, json_file)

    print(f'The list has been written to {file_path}.')


def write_file(file_path: str, data):
    if (len(data) <= 2):
        LOGGER.info(f"Query returned no results for {file_path}")
        return
        # print('here')
    LOGGER.info(f"Writing file {file_path}")
    # Path to the JSON file
    # Write the extracted list to a JSON file
    with open(file_path, 'w+') as file:
        file.write(data)

    print(f'The list has been written to {file_path}.')


def read_json_file(file_path):
    # LOGGER.info(f"Reading file {file_path}")
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path}")
        return None


def get_wikidata_label(item_id):
    query = f"""
    SELECT ?itemLabel
    WHERE {{
      wd:{item_id} rdfs:label ?itemLabel.
      FILTER(LANG(?itemLabel) = "en")
    }}
    """
    endpoint_url = "https://query.wikidata.org/sparql"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'application/json'
    }

    params = {
        'format': 'json',
        'query': query
    }

    response = requests.get(endpoint_url, headers=headers, params=params)
    data = response.json()
    if "results" in data and "bindings" in data["results"]:
        label = data["results"]["bindings"][0]["itemLabel"]["value"]
        return label
    else:
        return None


def format_labels(values):
    formatted_values = []
    if type(values) != str:
        for value in values:
            if 'http://www.wikidata.org/entity/' in value and 'statement' not in value:
                _ = value.replace('http://www.wikidata.org/entity/', '')
                try:
                    # LOGGER.info(f"getting label for {_}")
                    label = get_wikidata_label(_)

                    if label is not None:
                        formatted_values.append(label.replace('&', ''))
                except:
                    formatted_values.append(value)
                    # LOGGER.error(f"Failed to get label for {_}")
            else:
                formatted_values.append(value)
    else:
        if 'http://www.wikidata.org/entity/' in values and 'statement' not in values:
            _ = values.replace('http://www.wikidata.org/entity/', '')
            try:
                # LOGGER.info(f"getting label for {_}")
                label = get_wikidata_label(_)

                if label is not None:
                    formatted_values.append(label.replace('&', ''))
            except:
                formatted_values.append(values)
                # LOGGER.error(f"Failed to get label for {_}")
        else:
            formatted_values.append(values)
    if len(formatted_values) == 1:
        return formatted_values[0]
    return formatted_values


def extract_properties(file, target_properties=conf.PROPS):
    extracted_data = []
    data = read_json_file(file)
    for entry in data:
        language_uri = entry.get("Language", "")
        properties = entry.get("Properties", [])

        extracted_entry = {"Language": language_uri, "Properties": {}}

        for prop_entry in properties:
            prop_uri = prop_entry.get("Property", "")
            values = format_labels(prop_entry.get("Values", []))

            # Check if the property is in the list of target properties
            if prop_uri in target_properties:
                extracted_entry["Properties"][prop_uri] = values

        extracted_data.append(extracted_entry)

    return extracted_data
