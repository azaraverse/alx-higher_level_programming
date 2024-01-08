#!/usr/bin/python3
"""Lookup module
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object

    Args:
        obj: object
    """
    return dir(obj)
