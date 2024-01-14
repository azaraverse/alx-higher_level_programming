#!/usr/bin/python3
""" DEFINES BASE CLASS
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation of
        'list_dictionaries'

        Args:
            list_dictionaries (list): list of dictionaries.
        Returns:
            JSON string representation of the list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation of
        'list_objs' to a file

        Args:
            list_objs (list): list of instances that inherit of Base
        """
        filename = cls.__name__ + '.json'
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )
        # create file or open file if it exists in write mode
        with open(filename, 'w') as file:
            # write the json_string to the file
            file.write(json_string)
