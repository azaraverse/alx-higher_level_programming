#!/usr/bin/python3
"""subclass module that inherits Rectangle class and methods
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits attributes and methods of Rectangle."""
    def __init__(self, size):
        """init method instance for subclass Rectangle to Rectangle

        Args:
            size (int): size int
        """
        # set args to private
        self.__size = size
        # validate width and height int as positives
        super().integer_validator('size', size)
        super().__init__(size, size)

    def area(self):
        """Returns the area value."""
        return self.__size * self.__size
