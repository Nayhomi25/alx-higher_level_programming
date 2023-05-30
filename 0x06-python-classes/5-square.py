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

    def my_print(self):
        """ print out a square """

        if self.__size == 0:
            print()

        for x in range(self.__size):
            print("#" * self.__size)
