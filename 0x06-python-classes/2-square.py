#!/usr/bin/python3

"""
An empty Square class.
"""


class Square:
    """
    An empty class Square that defines a square.
    """
    def __init__(self, size=0):
        """Creates an instance of the Square class.

        Args:
            size (int): private instance attr of Square.
            returns to default 0.

        Raises:
            TypeError: when the value is not an integer
            ValueError: when value is less than 0
        """

        # handle integer
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        # handle negative values
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
