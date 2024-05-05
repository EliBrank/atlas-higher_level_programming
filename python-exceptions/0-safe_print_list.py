#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i, last_index = 0, 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            last_index = i
    except IndexError:
        return last_index
    if x > 0:
        print()
    return i
