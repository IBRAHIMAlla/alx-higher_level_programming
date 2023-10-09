#!/usr/bin/python3
"""
7-base_geometry module
"""


class BaseGeometry:
    """
    Depict base geometry.
    """
    def area(self):
        """
        Not yet implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Args:
            name: Parameter's name.
            value: Validate the parameter.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
