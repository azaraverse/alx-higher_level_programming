#!/usr/bin/python3
"""is_same_class module
"""


def is_same_class(obj, a_class):
    """is_same_class function

    Args:
        obj: object to check
        a_class: specified class

    Returns:
        True if the object is exactly an instance of the specified
    class, otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
