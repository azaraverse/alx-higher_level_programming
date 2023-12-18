#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # try to format the value as an integer using "{:d}"
        formattedValue = "{:d}".format(value)

        # print the formatted int, then a new line
        print(formattedValue)

        # return True, since the value has been correctly printed
        return (True)
    except ValueError:
        # if a ValueError occurs, it means the value is not an int
        # return False then
        return (False)
    except TypeError:
        # if a TypeError occurs, it means the type is not of int type
        # return False then
        return (False)
