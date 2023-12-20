#!/usr/bin/python3

"""
Python class that does as a given Python bytecode
"""

import math


class MagicClass:
    """
    A MagicClass class defined here
    """
    def __init__(self, radius=0) -> None:
        """
        Creates an instance of the MagicClass class

        Args (int):
            radius: radius passed as arg

        Raises:
            TypeError: when radius is not an int nor float
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        public instance method that handles the computation
        of the area of a circle.

        Returns (int): area of a circle
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        public instance method that handles the computation
        of the circumference of a circle.

        Returns (int): circumference of a circle
        """
        return (2 * math.pi) * self.__radius
