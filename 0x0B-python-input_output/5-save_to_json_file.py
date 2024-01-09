#!/usr/bin/python3
"""SAVE_TO_JSON_FILE MODULE
"""

import json


def save_to_json_file(my_obj, filename):
    """A function that writes an obj to a text file,
    using a JSON representation
    
    Args:
        my_obj (object): object to write to JSON file
        filename (str): file name of JSON file
    """
    with open(filename, 'w', encoding='UTF-8') as file:
        file.write(json.dumps(my_obj))
