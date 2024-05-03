#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Creates a new list of keys in alphabetical order
    sorted_keys = sorted(a_dictionary)
    for key in sorted_keys:
        # Accessing dict at [key] is like accessing list at [index]
        print("{}: {}".format(key, a_dictionary[key]))

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
