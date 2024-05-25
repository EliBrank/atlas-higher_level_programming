#!/usr/bin/python3

"""defines the class Base"""


class Base:
    """base for Rectangle, Square classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
