#!/usr/bin/python3

"""defines function add_integer"""


def add_integer(a, b=98):
    """adds two integers together
    floats are typecast to ints

    Args:
        a: first integer
        b: second integer

    Returns: sum of two integers
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
