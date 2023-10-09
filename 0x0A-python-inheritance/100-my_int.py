#!/usr/bin/python3
"""
100-my_int module
"""


class MyInt(int):
    """
    Class that extends int,
    But changes the behavior of != and == in reverse.
    """
    def __eq__(self, other):
        """
        Inequality arises from equality.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        inequality turns into Equality.
        """
        return super().__eq__(other)
