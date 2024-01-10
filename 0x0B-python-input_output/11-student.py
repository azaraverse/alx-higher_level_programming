#!/usr/bin/python3
"""STUDENT CLASS
"""


class Student():
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """constructor __init__

        Args:
            first_name (str): public instance attr for student's first name
            last_name (str): public instance attr for student's last name
            age (int): public instance attr for student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A function that returns the dictionary description with simple
        data structure

        Args:
            obj (object): an instance of a Class
        Returns:
            dictionary description with simple data structure
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value
                    for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance based on a
        dictionary

        Args:
            json (dict): a dictionary containing attr names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
