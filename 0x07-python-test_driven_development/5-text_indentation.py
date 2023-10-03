#!/usr/bin/python3
"""
Function for replacing certain characters with '\n\n'
"""


def text_indentation(text):
    """
    Prints a text, inserting 2 new lines after certain characters
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    mpt = text.replace(".", ".\n\n")
    mpt = mpt.replace(":", ":\n\n")
    mpt = mpt.replace("?", "?\n\n")
    p = mpt.splitlines(True)
    a = []
    for m in y:
        if m == "\n":
            a.append("\n")
        else:
            a.append(m.lstrip())
    print("".join(a), end="")
