#!/usr/bin/python3
""" Create getter and setter properties """


class Square:
    """ Private instance atrribute: size """
    def __init__(self, size=0):
        """ Initializes attribute size """
        self.__size = size

    @property
    def size(self):
        """ getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ initilizes atrribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns area of square """
        return int(self.__size) * int(self.__size)
