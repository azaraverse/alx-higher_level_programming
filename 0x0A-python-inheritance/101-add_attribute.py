#!/usr/bin/python3
"""add_attribute function that adds a new attribute to an object
"""


def add_attribute(obj, name, value):
    """a function that adds a new attr to an object if it's possible."""
    # use hasattr to check if given object (class in this case) has __dict__
    if hasattr(obj, '__dict__'):
        # object has __dict__ attr, so it can have new attributes
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
