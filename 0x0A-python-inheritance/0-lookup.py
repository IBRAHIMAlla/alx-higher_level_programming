#!/usr/bin/python3
"""
lookup - returns the list of an object's accessible attributes and methods
@obj: object
Return: list object
"""


def lookup(obj):
    """ list of obj """
    return dir(obj)
