#!/usr/bin/python3
"""Defines Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width=int, height=int, x=0, y=0, id=None):
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
    def width(self, width=int):
        """setter method for width attr of Rectangle class

        Args:
            width (int): width of the rectangle object
        """
        self.__width = width

    @property
    def height(self):
        """getter method for height attr of Rectangle class"""
        return self.__height

    @height.setter
    def height(self, height=int):
        """setter method for height attr of Rectangle class

        Args:
            height (int): height of the rectangle object
        """
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
        self.__y = y
