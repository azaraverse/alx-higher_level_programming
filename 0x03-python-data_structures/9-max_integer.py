#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    '''
    perform bubblesort operation to sort list
    items in ascending order.
    this efficiently sorts out the highest number
    '''
    i = len(my_list) - 1
    while i >= 1:
        j = 0
        while j < i:
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            j += 1
        i -= 1
    '''
    but i cannot tell if the bubblesort operation
    is as relevant. given the operation below in an
    attempt to return the highest number discards
    the bubblesort operation
    '''
    mxm = my_list[0]
    for n in my_list:
        if n > mxm:
            mxm = n
    return mxm
