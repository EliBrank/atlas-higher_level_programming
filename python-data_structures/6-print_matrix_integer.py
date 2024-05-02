#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        first_in_row = True
        for i in row:
            if first_in_row:
                print("{:d}".format(i), end='')
                first_in_row = False
            else:
                print(" {:d}".format(i), end='')
        print("")
