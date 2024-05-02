#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    print("{} ".format(num_args), end='')
    if num_args == 0:
        print("arguments.")
    elif num_args == 1:
        print("argument:")
    else:
        print("arguments:")

    if num_args > 0:
        for i in range(num_args):
            print("{}: {}".format(i + 1, argv[i + 1]))
