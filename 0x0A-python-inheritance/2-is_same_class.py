#!/usr/bin/python3
"""
2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
    is_same_class - verify whether an object is an exact instance of a specified class.
    Args:
        ibj: The object to verify.
        a_class: The class that matches the type of obj.
    Returns: If obj is exactly an instance of a_class - True,
            Otherwise - False.
    """
    return True if type(obj) is a_class else False
