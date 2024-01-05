#!/usr/bin/python3
"""list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak (list_of_integers)"""

    if list_of_integers is None or list_of_integers == []:
        return None
    m = 0
    i = len(list_of_integers)
    md = ((i - m) // 2) + m
    md = int(md)
    if i == 1:
        return list_of_integers[0]
    if i == 2:
        return max(list_of_integers)
    if list_of_integers[md] >= list_of_integers[md - 1] and\
            list_of_integers[md] >= list_of_integers[md + 1]:
        return list_of_integers[md]
    if md > 0 and list_of_integers[md] < list_of_integers[md + 1]:
        return find_peak(list_of_integers[md:])
    if md > 0 and list_of_integers[md] < list_of_integers[md - 1]:
        return find_peak(list_of_integers[:md])
