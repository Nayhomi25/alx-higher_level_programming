#!/usr/bin/python3
"""2-is_same_class.py"""


def is_same_class(obj, a_class):
    """checks if the object is instance of class
        Rturns: True if isinstance or false if fails
    """
    if type(obj) == a_class:
        return True
    return False
