#!/usr/bin/python3

def weight_average(my_list=[]):

    if my_list == []:
        return(0)

    numerator = 0
    denominator = 0

    for tpl in my_list:
        numerator += (tpl[0] * tpl[1])
        denominator += tpl[1]

    return(numerator / denominator)
