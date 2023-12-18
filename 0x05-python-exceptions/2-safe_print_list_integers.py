#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer_count = 0

    try:
        for i in range(x):
            # check if the element is an integer
            if isinstance(my_list[i], int):
                # print the integer on the same line
                print("{:d}".format(my_list[i]), end='')

                # increment the count of int printed to move to the next
                integer_count += 1
    except IndexError:
        # if an index error occurs, we have reached the end of our list
        pass
    except ValueError:
        pass
    except TypeError:
        pass
    # handle new line
    print()

    # return the real number of integers printed
    return (integer_count)
