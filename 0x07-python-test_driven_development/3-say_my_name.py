#!/usr/bin/python3
"""
print a phrase
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a phrase with:

    first_name: String that should be printed
    last_name: second string that should be printed

    Return: Formatted output containing strings.
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
