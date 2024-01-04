#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """defined function for matrix division."""
    # first check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    # check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
            )
    # check if element in matrix is a number
    if not all(
        isinstance(element, (int, float)) for row in matrix for element in row
    ):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
            )
    # check if each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    # create a new matrix for the result to be stored in...
    new_matrix = [
        [round(element / div, 2) for element in row] for row in matrix
        ]

    return new_matrix
