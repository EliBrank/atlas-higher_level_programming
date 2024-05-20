#!/usr/bin/python3

"""defines the function is_same_class"""


def is_same_class(obj, a_class):
    """checks if specified object is of specified class

    Returns: True if obj is of class a_class, else False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
