#!/usr/bin/python3

from sys import argv

"""
0 arguments.
1 argument:
1: Hello
6 arguments:
"""

if __name__ == "__main__":
    print("{} argument".format(len(argv)), end='')
    if len(argv) == 0:
        print("s.")
    if len(argv) == 1:
        print(":")
    else:
        print("s:")

    if len(argv) > 0:
        for i in range(len(argv)):
            print("{}: {}".format(i + 1, argv[i]))
