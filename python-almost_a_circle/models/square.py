#!/usr/bin/python3

"""defines the class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """a square shape which can be modified and printed"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiates Square"""
        super().__init__(size, size, x, y, id)
