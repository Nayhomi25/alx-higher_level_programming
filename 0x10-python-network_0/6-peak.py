#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    lsize = len(list_of_integers)
    if lsize == 1:
        return list_of_integers[0]
    elif lsize == 2:
        return max(list_of_integers)

    avg = int(lsize / 2)
    peak = list_of_integers[avg]
    if peak > list_of_integers[avg - 1] and peak > list_of_integers[avg + 1]:
        return peak
    elif peak < list_of_integers[avg - 1]:
        return find_peak(list_of_integers[:avg])
    else:
        return find_peak(list_of_integers[avg + 1:])
