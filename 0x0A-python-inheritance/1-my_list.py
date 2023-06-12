#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """A class inheriting from list"""

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
