#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    k_list = sorted(new_dir.keys())

    for m in k_list:
        new_dir[m] *= 2

    return (new_dir)
