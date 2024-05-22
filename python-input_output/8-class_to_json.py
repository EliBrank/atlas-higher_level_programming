#!/usr/bin/python3

"""defines the function class_to_json"""


def class_to_json(obj):
    """creates dictionary ready to be serialized into json"""
    return obj.__dict__
