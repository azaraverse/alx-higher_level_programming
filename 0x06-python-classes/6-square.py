#!/usr/bin/python3

"""
An empty Square class.
"""


class Square:
    """
    An empty class Square that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

    def area(self):
        """
        public instance method that handles the computation
        of the area of a square.

        Returns (int): area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter method to retrieve the size of the square.

        Returns (int): retrieved size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method to set the size of the square.

        Args (int):
            value: size of square to set.
        """
        # handle integer
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            self.__size = value

    def my_print(self):
        """
        public instance method that prints in stdout the square
        with the character # and considering the position /
        cordinates.
        """
        # handle '#' and position when size is greater than 0
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    @property
    def position(self):
        """
        getter method to retrieve the position of the square.

        Returns (int): retrieved position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter method to set the position of the square.

        Args (int):
            value: position to set.
        Raises:
            TypeError: if value is not a tuple of two positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif sum(1 for i in value if isinstance(i, int) and i >= 0) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (value[0] < 0 and value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
