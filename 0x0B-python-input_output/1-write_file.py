#!/usr/bin/python3
"""WRITE FILE MODULE
"""


def write_file(filename='', text=''):
    """A function that writes to a text file

    Args:
        filename (str): name of file to write to
        text (str): text to write
    Returns:
        string count of written text to stdout
    """
    # open file with 'r' read-only mode
    written = 0
    with open(filename, 'w', encoding='UTF-8') as file:
        written += file.write(text)
    return written
