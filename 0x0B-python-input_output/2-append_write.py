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
    written = 0
    # open file with 'a' append mode
    with open(filename, 'a', encoding='UTF-8') as file:
        written += file.write(text)
    return written
