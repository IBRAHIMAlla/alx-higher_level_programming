#!/usr/bin/python3
"""
2-append_write.py
"""


def append_write(filename="", text=""):
    """
    write_file - appends a string at the end of a text (UTF8),
                && returns the number of characters:
    Args:
        filename: file's name
        text: text
    Return: number of bytes written.
    """
    with open(filename, mode="a", encoding="UTF-8") as m:
        return (m.write(text))
