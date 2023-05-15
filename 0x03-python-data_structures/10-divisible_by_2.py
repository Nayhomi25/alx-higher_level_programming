#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    modulo = []

    for i in my_list:
        if i % 2 == 0:
            modulo.append(True)
        else:
            modulo.append(False)

    return(modulo)
