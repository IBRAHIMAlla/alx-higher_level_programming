#!/usr/bin/python3
""" class Square."""


class Square:
    """  class defined
        Attributes:
            size (int): Size of square
            position (tuple): position of space and new lines
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes
        Args:
            size (int): size
            postion(tuple): postion
        Returns:
            None
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        get postion attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter of position
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        get area
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for m in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
