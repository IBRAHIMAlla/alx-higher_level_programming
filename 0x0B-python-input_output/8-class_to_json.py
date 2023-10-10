#!/usr/bin/python3
"""8-class_to_json Module
"""


def class_to_json(obj):
    """Returns the dictionary description with data structure
    [list, dictionary, string, integer and boolean] for JSON serialization
    of an object
    Args:
        obj: an instance
    """
    return vars(obj)
