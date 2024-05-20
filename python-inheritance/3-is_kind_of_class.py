#!/usr/bin/python3

"""defines the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """checks if specified object is descendant of specified class

    Returns: True if obj is of class that inherits from a_class, else False
    """

    return isinstance(obj, a_class)
