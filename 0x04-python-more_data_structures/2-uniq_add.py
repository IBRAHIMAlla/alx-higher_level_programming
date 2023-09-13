#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set(my_list)
    n = 0

    for m in uniq_int:
        n += m

    return (n)
