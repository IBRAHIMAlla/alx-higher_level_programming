#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """Creates an Object from “JSON file”
    Args:
        filename: file's name
    Returns: object decoded from filename
    """
    with open(filename, "r", encoding="utf-8") as m:
        o = json.load(m)

    return o
