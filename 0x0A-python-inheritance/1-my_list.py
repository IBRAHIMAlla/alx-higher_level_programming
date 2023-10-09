#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """
    MyList Offspring of a list
    """
    def print_sorted(self):
        """
        print_sorted - Sorts the list and then prints it
        """
        print(sorted(self))
