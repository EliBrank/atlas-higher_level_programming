#!/usr/bin/python3

"""defines the class Student"""


class Student:
    """defines Student instances"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """creates dictionary ready to be serialized into json

        Args:
            attrs: attributes to return in dictionary (all if None)

        Returns: Python dictionary of attributes specified
        """
        if attrs is None:
            return self.__dict__
        else:
            return ({attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)})

    def reload_from_json(self, json):
        "
