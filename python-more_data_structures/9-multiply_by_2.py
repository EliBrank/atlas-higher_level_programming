#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    two_dict = a_dictionary.copy()
    for i in two_dict:
        two_dict[i] *= 2
    return two_dict
