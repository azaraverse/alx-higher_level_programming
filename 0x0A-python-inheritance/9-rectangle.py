#!/usr/bin/python3
"""subclass module that inherits BaseGeometry class and methods
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits attributes and methods of BaseGeometry."""
    def __init__(self, width, height):
        """init method instance for subclass Rectangle to BaseGeometry

        Args:
            width (int): width int
            height (int): height int
        """
        # set args to private
        self.__width = width
        self.__height = height
        # validate width and height int as positives
        super().integer_validator('width', width)
        super().integer_validator('height', height)

    def area(self):
        """Returns the area value."""
        return self.__width * self.__height
    
    def __str__(self):
        """Returns rectangle description."""
        return f'[{type(self).__name__}] {self.__width}/{self.__height}'
