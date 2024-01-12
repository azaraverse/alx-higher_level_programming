#!/usr/bin/python3
""" DEFINES BASE CLASS
"""


class Base():
    """Base Class for other classes to avoid code duplication"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base Class

        Args:
            id (int): ID attribute of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
