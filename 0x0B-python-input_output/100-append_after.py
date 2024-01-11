#!/usr/bin/python3
"""APPEND_AFTER MODULE
"""


def append_after(filename='', search_string='', new_string=''):
    """A function that inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename (str): name of the file to use
        search_string (str): string to search for in filename
        new_string (str): string to print after finding search_string
    """
    # open file in 'r' and 'w' mode
    with open(filename, 'r+', encoding='UTF-8') as file:
        read_line = file.readlines()

        for i, line in enumerate(read_line):
            if search_string in line:
                read_line[i] += new_string

        # return to top of file and write changes
        file.seek(0)
        file.writelines(read_line)
