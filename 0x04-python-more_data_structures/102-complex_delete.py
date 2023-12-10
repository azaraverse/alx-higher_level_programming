#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        values = list(
            filter(lambda *x: x[0][1] == value, a_dictionary.items())
            )

        for key, value in values:
            del a_dictionary[key]
    return a_dictionary
