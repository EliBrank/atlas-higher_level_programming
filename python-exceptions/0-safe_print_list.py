#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 1
    if x == 0:
        return 0
    try:
        for i in range(x):
            print(my_list[i], end='')
        print()
        return i + 1
    except IndexError:
        print()
        return i


my_list = [4, 3, 1, 8, 6]

nb_print = safe_print_list(my_list, 0)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
