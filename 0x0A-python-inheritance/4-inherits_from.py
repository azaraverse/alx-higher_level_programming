#!/usr/bin/python3
"""inherits_from module
"""


def inherits_from(obj, a_class):
    """inherits_from function

    Args:
        obj: object to check
        a_class: specified class

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class,
        otherwise False
    """
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    else:
        return False
