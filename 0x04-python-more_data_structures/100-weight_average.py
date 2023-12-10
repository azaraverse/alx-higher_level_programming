#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    return (
        sum(list(map(lambda *x: x[0][0] * x[0][1], my_list)))
        / sum(list(map(lambda *x: x[0][1], my_list)))
    )
