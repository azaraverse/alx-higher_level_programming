#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        # try to format the value as an integer using "{:d}"
        formattedValue = "{:d}".format(value)

        # print the formatted int, then a new line
        print(formattedValue)

        # return True, since the value has been correctly printed
        return (True)
    except ValueError as err:
        # if a ValueError occurs, it means the value is not an int
        # handle error writing to stdout
        err = "Exception: " + str(err) + "\n"
        sys.stderr.write(err)

        # return False then
        return (False)
