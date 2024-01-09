#!/usr/bin/python3
"""SAVE_TO_JSON_FILE MODULE
"""

import json


def load_from_json_file(filename):
    """A function that creates an obj from a JSON file.

    Args:
        filename (str): file name of JSON file
    Returns:
        object: The python object created from the JSON file.
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data
