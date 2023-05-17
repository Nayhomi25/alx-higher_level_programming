#!/usr/bin/python3
def search_replace(my_list, search, replace):

    fake_list = my_list.copy()

    for x in range(len(fake_list)):
        if fake_list[x] == search:
            fake_list[x] = replace
    return(fake_list)
