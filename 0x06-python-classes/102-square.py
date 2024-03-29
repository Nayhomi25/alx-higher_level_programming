#!/usr/bin/python3
""" Defines the class square"""


class Square:
    """
    Defines a square
    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """ Retrieve size of square """

        return self.__size

    @size.setter
    def size(self, value):
        """ set value of size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    def area(self):
        """ calculates area of square"""
        return(self.__size ** 2)

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
