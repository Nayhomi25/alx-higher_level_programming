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
