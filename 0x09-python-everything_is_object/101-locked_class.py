#!/usr/bin/python3
"""
An empty class
"""


class LockedClass:
    """Empty class but prevents user from dynamically creating new instance
    attributes, execpt it is called 'first_name'
    """
    __slots__ = ['first_name']

    # def __init__(self, first_name) -> None:
    #    self.first_name = first_name
