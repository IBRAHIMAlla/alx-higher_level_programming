#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of lists
        Args:
            n (int): number of lists
        Returns: list of lists
    """
    r = [[1 for y in range(m + 1)] for m in range(n)]
    for n in range(n):
        for m in range(n - 1):
            r[n][m + 1] = sum(r[n - 1][m:m + 2])
    return r
