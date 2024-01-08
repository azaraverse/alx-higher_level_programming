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
