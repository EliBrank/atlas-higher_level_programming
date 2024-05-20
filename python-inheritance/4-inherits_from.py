#!/usr/bin/python3

"""defines the function inherits_from"""


def inherits_from(obj, a_class):
    """checks if specified object is of sub-class of specified class

    Returns: True if obj is of sub-class for a_class, else False
    """

    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
