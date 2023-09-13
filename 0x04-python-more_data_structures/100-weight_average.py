#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_s = 0
    total_w = 0

    for s, w in my_list:
        total_s += s * w
        total_w += w

    if total_w == 0:
        return 0
    return (total_s / total_w)
