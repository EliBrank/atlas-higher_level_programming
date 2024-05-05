#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    print_ct = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            print_ct += 1
        print()
    except IndexError:
        pass
    finally:
        return print_ct

my_list = [4, 3, 1, 8, 6]

nb_print = safe_print_list(my_list, 0)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
