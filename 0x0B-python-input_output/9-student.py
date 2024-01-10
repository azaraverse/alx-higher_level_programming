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

    def to_json(self):
        """A function that returns the dictionary description with simple
        data structure

        Args:
            obj (object): an instance of a Class
        Returns:
            dictionary description with simple data structure
        """
        return self.__dict__
