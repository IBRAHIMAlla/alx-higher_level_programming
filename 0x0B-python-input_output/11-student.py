#!/usr/bin/python3
"""11-student Module
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
        if type(attrs) == list and all([type(s) == str for s in attrs]):
            return {key: value for key, value in vars(self).items()
                    if key in attrs}

        return vars(self)

    def reload_from_json(self, json):
        """Replaces all attributes"""
        for k, v in json.items():
            setattr(self, k, v)
