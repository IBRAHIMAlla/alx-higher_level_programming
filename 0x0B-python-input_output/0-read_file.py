#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - reads a text file  && prints it to stdout
    Args:
        filename: file's name
    """
    with open(filename, "r", encoding="UTF-8") as m:
        for line in m:
            print(line, end="")
