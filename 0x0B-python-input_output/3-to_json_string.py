#!/usr/bin/python3
"""TO_JSON_STRING MODULE
"""

import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of a python
    string.

    Args:
        my_obj (object): object to represent in JSON
    Returns:
        JSON representation of a python string
    """
    json_represent = json.dumps(my_obj)
    return json_represent
