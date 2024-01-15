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
            f'[{self.__class__.__name__}] ({self.id}) '
            f'{self.x}/{self.y} - {self.width}'
        )

    def update(self, *args, **kwargs):
        """Assigns positional arguments and key-worded arguments attrs

        Args:
            *args: variable or positional arguments
            **kwargs: key-worded arguments
        """
        # if *arguments exist and is not empty, update attrs
        # based on their positions
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        # if *args is empty, update attrs based on **kwargs
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
