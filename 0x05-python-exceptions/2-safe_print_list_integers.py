#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    prtd = 0
    for m in range(0, x):
        try:
            print("{:d}".format(my_list[m]), end="")
            prtd += 1
        except (ValueError, TypeError):
            continue
    print()
    return prtd
