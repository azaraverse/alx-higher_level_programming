#!/usr/bin/python3
"""APPEND FILE MODULE
"""


def append_write(filename='', text=''):
    """A function that appends a str to the end of a text file

    Args:
        filename (str): name of file to append text to
        text (str): text to append
    Returns:
        string count of appended text to stdout
    """
    # open file with 'r' read-only mode
    written = 0
    with open(filename, 'a', encoding='UTF-8') as file:
        written += file.write(text)
    return written
