#!/usr/bin/python3

"""defines the class Base"""

import json


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

    @staticmethod
    def from_json_string(json_string):
        """returns JSON string representation of json_string"""

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves each object in list_objs to JSON file"""

        filename = f"{cls.__name__}.json"

        json_list = []
        with open(filename, "w") as f:
            if list_objs is not None:
                for obj in list_objs:
                    json_list.append(obj.to_dictionary())
                f.write(cls.to_json_string(json_list))
            else:
                f.write(cls.to_json_string([]))
