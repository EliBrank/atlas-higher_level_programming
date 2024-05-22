#!/usr/bin/python3

"""defines the class Student"""


class Student:
    """defines Student instances"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """creates dictionary ready to be serialized into json

        Returns: Python dictionary of attributes
        """

        return self.__dict__
