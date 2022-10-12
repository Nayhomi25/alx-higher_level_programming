#!/usr/bin/python3
""" print a square to stdout """


class Square:
    """ Private instance atrribute: size """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes attribute size """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Initializes attribute position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print method"""
        if (self.size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(0, self.size):
                for e in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
