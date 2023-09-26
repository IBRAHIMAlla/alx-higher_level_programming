#!/usr/bin/python3
"""magic class"""
import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """area function"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi) * self.__radius
