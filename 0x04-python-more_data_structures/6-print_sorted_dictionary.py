#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary.keys())
    for m in sorted_list:
        v = a_dictionary[m]
        print(f"{m}: {v}")
