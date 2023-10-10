#!/usr/bin/python3
"""
Module for append_after method.
"""


def append_after(filename="", search_string="", new_string=""):
    '''Method for inserting.'''
    ln = []
    with open(filename, "r", encoding="utf-8") as m:
        ln = m.readlines()
        y = 0
        while y < len(ln):
            if search_string in ln[y]:
                ln[y:y + 1] = [ln[y], new_string]
                y += 1
            y += 1
    with open(filename, "w", encoding="utf-8") as m:
        m.writelines(ln)
