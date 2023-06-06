#!/usr/bin/python3
""" Add_integer.py """


def add_integer(a, b=98):
    """a function that adds two integers

       Returns an integer ith the result of the addition
    """
    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
