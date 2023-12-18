#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0

    try:
        for i in range(x):
            # try to access the element at index i
            element = my_list[i]
            # now print the element on the same line
            print(element, end="")
            # increment the count of the elements to next
            elements_printed += 1
    except IndexError:
        # if an indexerror occurs, means we have reach the end of the list
        pass
    # print a new line after printing the elements
    print()

    # return the real number of elements printed
    return (elements_printed)
