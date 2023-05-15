#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    fake_list = my_list.copy()

    if idx < 0 or idx > len(my_list) - 1:
        return(fake_list)
    else:
        fake_list[idx] = element
    return fake_list
