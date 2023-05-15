#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        tsil = my_list
        tsil.reverse()
        
        for x in tsil:
            print("{:d}".format(x))
