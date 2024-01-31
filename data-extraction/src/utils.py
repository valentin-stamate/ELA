import json

from src.logger import LOGGER


def write_json_file(file_path: str, data: list):
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
    #LOGGER.info(f"Reading file {file_path}")
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
