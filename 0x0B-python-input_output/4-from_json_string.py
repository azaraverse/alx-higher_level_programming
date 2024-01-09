#!/usr/bin/python3
"""FROM_JSON_STRING MODULE
"""

import json


def from_json_string(my_obj):
    """A function that returns an object represented by a JSON
    string.

    Args:
        my_obj (object): object to represent in JSON
    Returns:
        an object represented by a JSON string.
    """
    obj_represent = json.loads(my_obj)
    return obj_represent
