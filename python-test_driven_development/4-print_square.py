#!/usr/bin/python3

"""defines the function print_square"""


def print_square(size):
    """prints ASCII square composed of "#" to stdout

    Args:
        size: length of each side of square
    """

    if isinstance(size, float):
        if size >= 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
