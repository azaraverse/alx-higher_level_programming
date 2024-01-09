#!/usr/bin/python3
"""READ FILE MODULE
"""


def read_file(filename=''):
    """A function that reads a text file

    Args:
        filename (str): name of file to read
    Returns:
        printed text of read text to stdout
    """
    # open file with 'r' read-only mode
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            print(line, end='')
