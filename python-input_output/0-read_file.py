#!/usr/bin/python3

"""defines the function read_file"""


def read_file(filename=""):
    """opens, reads, prints file specified to stdout"""
    with open(filename, "r") as f:
        f_contents = f.read()
        print(f_contents, end="")
