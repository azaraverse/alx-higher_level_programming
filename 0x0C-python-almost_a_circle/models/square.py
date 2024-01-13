#!/usr/bin/python3
"""Defines the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor

        Args:
            size (int): size of the square (width or height)
            x (int): x-coordinate of the square
            y (int): y-coordinate of the square
            id (int): ID attribute of the object
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size attr of square class"""
        return self.width

    @size.setter
    def size(self, size):
        """setter method for size attr of square class

        Args:
            size (int): size of the square object
        """
        self.width = size
        self.height = size

    def __str__(self):
        """Return the string representation of the square instance"""
        return (
            f'[Square] ({self.id}) '
            f'{self.x}/{self.y} - {self.width}'
        )
