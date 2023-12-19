#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for i in range(list_length):
        try:
            element1 = my_list_1[i]
            element2 = my_list_2[i] if i < len(my_list_2) else None

            # check if both elements are numbers
            # if not (isinstance(element1, (int, float))
            # and isinstance(element2, (int, float))):
            # raise TypeError("wrong type")

            # check if the divisor is not zero
            if element2 == 0:
                raise ZeroDivisionError("division by 0")

            # do division and append result to the list
            res_list.append(element1 / element2)

        except TypeError:
            print("wrong type")
            res_list.append(0)
        except ZeroDivisionError as err:
            print(err)
            res_list.append(0)
        except IndexError:
            print("out of range")
            res_list.append(0)
    # return the list
    return (res_list)
