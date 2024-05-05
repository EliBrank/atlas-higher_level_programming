#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    print_ct = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            print_ct += 1
    except IndexError:
        pass
    finally:
        print()
        return print_ct


my_list = [1, 2, 3, 4]

nb_print = safe_print_list(my_list, len(my_list) + 1)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, 0)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
