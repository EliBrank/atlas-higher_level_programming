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
