#!/usr/bin/python3
"""Class BaseGeometry
"""


class BaseGeometry():
    """Class BaseGeometry"""
    def __init__(self, name=str, value=int) -> None:
        """Init instance created.

        Args:
            name (str): arg 1
            value (int): arg 2
        """
        self.name = name
        self.value = value

    def area(self):
        """area function: empty

        Raises:
            Exception: No implementation
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator function

        Args:
            name: arg1
            value: arg2

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        # validate value is an integer
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')

        # validate value is greater than 0
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
