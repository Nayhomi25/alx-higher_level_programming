#!/usr/bin/python3
"""4-print_square.py"""


def print_square(size):
    """ Prints a square with symbol # """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()

    for x in range(size):
        print("#" * size)
