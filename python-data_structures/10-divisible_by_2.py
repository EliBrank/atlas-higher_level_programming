#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    div_two_list = my_list[:]
    for i in range(len(my_list)):
        if abs(my_list[i]) % 2 == 0:
            div_two_list[i] = True
        else:
            div_two_list[i] = False
    return div_two_list
