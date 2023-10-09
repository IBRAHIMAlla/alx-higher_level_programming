#!/usr/bin/python3
"""
3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class: Verify whether an object is an instance,
                    or an instance of a class inherited.
    Args:
        obj: The object to verify.
        a_class: The class that matches the type of obj.
    Returns: If obj is an instance or inherited instance of a_class - True,
            Otherwise - False.
    """
    return isinstance(obj, a_class)
