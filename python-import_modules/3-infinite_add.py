#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    total = 0
    num_args = len(argv) - 1
    for i in range(num_args):
        total += int(argv[i + 1])
    print(total)
