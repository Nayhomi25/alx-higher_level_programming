#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    x = 0,
    new_list = []

    for x in range(0, list_length):
        div = 0

        try:
            div = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
            x += 1
    return (new_list)
