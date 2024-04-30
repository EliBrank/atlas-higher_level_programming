#!/usr/bin/python3

def print_last_digit(number):
    n = abs(number) % 10
    if n < 0:
        print(n * -1, end='')
        return n * -1
    else:
        print(n, end='')
        return n
