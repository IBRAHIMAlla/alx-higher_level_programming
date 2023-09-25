#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    m = 0
    prtd = 0
    for m in range(0, x):
        try:
            print("{}".format(my_list[m]), end="")
            prtd += 1
        except:
            continue
    print()
    return prtd
