#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for a in range(0, len(my_string)):
        if my_string[a] != 'c' and my_string[a] != 'C':
            new_string += my_string[a]
    return new_string
