#!/usr/bin/python3
"""Defines a peak-finding algorithm."""
def find_peak(list_of_integers):

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    lidx = int(len(list_of_integers) / 2)

    if lidx != len(list_of_integers) - 1:
        if list_of_integers[lidx - 1] < list_of_integers[lidx] and\
           list_of_integers[lidx + 1] < list_of_integers[lidx]:
            return list_of_integers[lidx]
    else:
        if list_of_integers[lidx - 1] < list_of_integers[lidx]:
            return list_of_integers[lidx]
        else:
            return list_of_integers[lidx - 1]

    if list_of_integers[lidx - 1] > list_of_integers[lidx]:
        a_list = list_of_integers[0:lidx]
    else:
        a_list = list_of_integers[lidx + 1:]

    return find_peak(a_list)
