#!/usr/bin/python3
"""12-pascal_triangle
"""


def fact(m):
    """Returns the factorial"""
    if m == 0:
        return 1
    return m * fact(m - 1)


def comb(a, b):
    """Returns the res"""
    return fact(a) / (fact(b) * fact(a - b))


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    return [[int(comb(c, m)) for m in range(c + 1)] for c in range(n)]
