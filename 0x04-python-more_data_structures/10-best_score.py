#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    b_dict = list(a_dictionary.keys())[0]
    max_score = a_dictionary[b_dict]

    for x, y in a_dictionary.items():
        if y > max_score:
            max_score = y
            b_dict = x
    return(b_dict)
