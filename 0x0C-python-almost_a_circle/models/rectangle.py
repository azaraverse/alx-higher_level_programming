#!/usr/bin/python3
"""Defines Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor

        Args:
            width (int): width of the rectangle object
            height (int): height of the rectangle object
            x (int): x coordinate of rectangle object
            y (int): y coordinate of rectangle object
            id (int): ID attribute of object
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method for width attr of Rectangle class"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter method for width attr of Rectangle class

        Args:
            width (int): width of the rectangle object
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """getter method for height attr of Rectangle class"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method for height attr of Rectangle class

        Args:
            height (int): height of the rectangle object
        """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """getter method for x coordinate of Rectangle class"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for x coordinate of Rectangle class

        Args:
            x (int): x coordinate of rectangle object
        """
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """getter method for y coordinate of Rectangle class"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y coordinate of Rectangle class

        Args:
            y (int): y coordinate of rectangle object
        """
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y
