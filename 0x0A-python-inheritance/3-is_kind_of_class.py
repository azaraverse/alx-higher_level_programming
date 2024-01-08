#!/usr/bin/python3
"""is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class function

    Args:
        obj: object to check
        a_class: specified class

    Returns:
        True if the object is an instance of, or instance of the class
        that inherited from the specified class, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
