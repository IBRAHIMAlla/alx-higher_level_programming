#!/usr/bin/python3
"""
10-square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Depict a square.
    Derives from Rectangle.
    """
    def __init__(self, size):
        """
        init - Instantiates a Square.
        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area - returns area of a square
        """
        return self.__size ** 2
