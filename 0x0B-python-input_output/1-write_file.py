#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    write_file - writes a string to a text (UTF8),
                && returns the number of characters written:
    Args:
        filename: file's name
        text: text
    Return: number of bytes written.
    """
    with open(filename, mode="w", encoding="UTF-8") as m:
        return (m.write(text))
