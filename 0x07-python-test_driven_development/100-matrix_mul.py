#!/usr/bin/python3
"""matrix_mul module
"""


def matrix_mul(m_a, m_b):
    """matrix_mul multiplies two matrices.

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix.

    Returns:
        list of lists: resulting matrix mul

    Raises:
        TypeError:  if m_a or m_b is not a list
                    if m_a or m_b is not a list of lists
                    if one element of m_a or m_b is not an int or float
                    if m_a or m_b is not a rectangle
        ValueError: if m_a or m_b is empty
                    if m_a and m_b can't be multiplied
    """
    # check if m_a or m_b is not a list
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    # check if m_a or m_b is not a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    # check if m_a or m_b is empty
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    # check if any element of m_a or m_b is not an int or float
    if any(
        not isinstance(element, (int, float)) for row in m_a for element in row
    ):
        raise TypeError('m_a should contain only integers or floats')
    if any(
        not isinstance(element, (int, float)) for row in m_b for element in row
    ):
        raise TypeError('m_b should contain only integers or floats')

    # check if m_a or m_b is not a rectangle, i.e must have same size
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    # check if m_a or m_b can not be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # perform matrix multiplcation
    result = [[
        sum(
            a * b for a, b in zip(row_a, col_b)
            ) for col_b in zip(*m_b)] for row_a in m_a
        ]
    return result
