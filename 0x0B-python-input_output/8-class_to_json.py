#!/usr/bin/python3
"""CLASS_TO_JSON MODULE
"""


def class_to_json(obj):
    """A function that returns the dictionary description with simple
    data structure

    Args:
        obj (object): an instance of a Class
    Returns:
        dictionary description with simple data structure
    """
    return obj.__dict__
