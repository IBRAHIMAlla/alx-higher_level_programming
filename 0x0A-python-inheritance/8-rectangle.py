#!/usr/bin/python3
"""
8-rectangle module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Depict a rectangle.
    Derives from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Instantiates an instance.
        Args:
            width: Rectangle's width
            height: Rectangle's height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
