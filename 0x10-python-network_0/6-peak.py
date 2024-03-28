#!/usr/bin/python3
'''a function that finds a peak in a list of unsorted integers
'''


def find_peak(list_of_integers):
    '''Finds a peak from a list of unsorted integers

    Args:
        list_of_integers (int): list of unsorted integers
    Return:
        peak integer (int): peak element found in the list
    Complexity:
        O(n)
    '''

    if not list_of_integers:
        return None

    list_of_integers.sort()
    return list_of_integers[-1]
