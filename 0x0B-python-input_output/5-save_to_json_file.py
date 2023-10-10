#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        my_obj: python object
        filename: file's name
    Returns: None
    """
    with open(filename, 'w', encoding="utf-8") as m:
        json.dump(my_obj, m)
