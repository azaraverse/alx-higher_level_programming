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

    def area(self):
        """Area method that returns the area value of the Rectangle object"""
        return self.__width * self.__height

    def display(self):
        """print the Rectangle instance using the character '#'."""
        # print empty lines for y-axis (coordinate)
        for _ in range(self.y):
            print()

        # print spaces for the x-axis then attach '#' character
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self) -> str:
        """Return the string representation of the Rectangle instance."""
        return (
            f'[{self.__class__.__name__}] ({self.id}) '
            f'{self.x}/{self.y} - {self.width}/{self.height}'
        )

    def update(self, *args, **kwargs):
        """Assigns arguments to id, width, height, x and y attrs.

        Args:
            *args: variable number of arguments
            **kwargs: key-worded arguments
        """
        # if *arguments exist and is not empty, update attrs
        # based on their positions
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        # if *args is empty, update attrs based on **kwargs
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
