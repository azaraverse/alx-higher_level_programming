#!/usr/bin/python3
"""
A function that prints a square with the character '#'.
"""


def print_square(size):
    """function definition for print_square().

    Args:
        size (int): the size length of the square.

    """
    # check if size is not an integer
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    else:
        for _ in range(size):
            print('#' * size)
