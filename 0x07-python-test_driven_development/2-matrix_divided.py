#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
"""


def matrix_divided(matrix, div):
    """
    Division on all elements within the matrix using div
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    z = None
    for m in matrix:
        if type(m) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if z is None:
            z = len(m)
        elif z != len(m):
            raise TypeError("Each row of the matrix must have the same size")
        for y in m:
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(y / div, 2) for y in m] for m in matrix]
