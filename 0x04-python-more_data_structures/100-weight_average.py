#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == 0:
        return (0)

    ave = 0
    div = 0
    for tul in my_list:
        ave += (tul[0] * tul[1])
        div += tul[1]
    return (ave / div)
