#!/usr/bin/python3
"""
A rectangle class
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Creates an instance of the rectangle class
        Args:
            width (int): an integer that stores our width value
            height (int): an int that stores our height value
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: private instance that retrieves width value
        Args:
            width (int): int that stores width value retrieved
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width: property setter for width
        Args:
            value: sets value of width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width < 0
        """
        # handle TypeError
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        """height: private instance that retrieves height value
        Args:
            height (int): int that stores height value retrieved
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height: property setter for height
        Args:
            value: sets value of height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height < 0
        """
        # handle TypeError
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
