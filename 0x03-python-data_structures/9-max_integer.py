#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return (None)

    b = my_list[0]
    for m in range(len(my_list)):
        if my_list[m] > b:
            b = my_list[m]

    return (b)
