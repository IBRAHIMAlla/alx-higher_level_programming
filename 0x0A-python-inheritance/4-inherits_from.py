#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    inherits_from - Verifies whether an object is an instance inherited from a class.
    Args:
        obj: The object to verify.
        a_class: The class that matches the type of obj.
    Returns: If obj is an inherited instance of a_class - True,
            Otherwise - False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
