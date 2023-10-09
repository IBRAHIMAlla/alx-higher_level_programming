#!/usr/bin/python3
"""
101-add_attribute module
"""


def add_attribute(an_obj, an_attr, a_value):
    """
    Verifies the feasibility of adding an attribute an_attr with the value a_value to an_obj.
    Args:
        - an_obj: Object to which the attribute should be added
        - an_attr: attribute's name
        - a_value: Attribute value to be added
    """

    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)
