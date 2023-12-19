#!/usr/bin/python3
def division(a, b):
    # init res with 0
    res = 0

    try:
        # try division
        res = a / b
        # handle 0 division error
    except ZeroDivisionError:
        print("division by 0")
        # handle type error
    except TypeError:
        print("wrong type")
    finally:
        # return result of division
        return res


def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for i in range(list_length):
        try:
            element1 = my_list_1[i]
            element2 = my_list_2[i]

            res_list.append(division(element1, element2))
        except IndexError:
            print("out of range")
            res_list.append(0)
    return (res_list)
