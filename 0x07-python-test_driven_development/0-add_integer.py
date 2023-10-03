#!/usr/bin/python3
"""
Function to adding two integers
"""


def add_integer(a, b=98):
    """The arguments to add.

    a: One of the numbers
    b: The other number

    Return: int(a + b)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
