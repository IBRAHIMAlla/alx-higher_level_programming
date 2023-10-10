#!/usr/bin/python3
"""10-student Module
"""


class Student:
    """Class student"""

    def __init__(self, first_name, last_name, age):
        """Initialises the first_name && last_name && age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary"""
        if type(attrs) == list and all([type(m) == str for m in attrs]):
            return {k: v for k, v in vars(self).items()
                    if k in attrs}

        return vars(self)
