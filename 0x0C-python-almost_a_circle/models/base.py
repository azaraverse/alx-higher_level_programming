#!/usr/bin/python3
""" DEFINES BASE CLASS
"""
import json
import models.rectangle as rectangle


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

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the JSON string
        representation 'json_string'

        Args:
            json_string (str): string representing a list of dictionaries
        Returns:
            List if the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all attrs
        already set

        Args:
            **dictionary (dict): key-worded argument
        Returns:
            an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = rectangle.Rectangle(5, 10)
        else:
            raise ValueError(f'Unsupported class: {cls.__name__}')
        
        dummy_instance.update(**dictionary)
        return dummy_instance
