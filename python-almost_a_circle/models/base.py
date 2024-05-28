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
        """converts JSON string to python objects

        Args:
            json_string: JSON string to be converted

        Returns: Python object representation of JSON string
        """

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts python dictionaries to JSON string

        Args:
            list_dictionaries: python dictionaries to be converted

        Returns: JSON string representation of dictionaries list
        """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves each object in list_objs to JSON file

        Args:
            list_objs: python objects to be converted and saved
        """

        filename = f"{cls.__name__}.json"

        json_list = []
        with open(filename, "w") as f:
            if list_objs is not None:
                for obj in list_objs:
                    json_list.append(obj.to_dictionary())
                f.write(cls.to_json_string(json_list))
            else:
                f.write(cls.to_json_string([]))

    @classmethod
    def create(cls, **dictionary):
        """uses dictionary values to update newly created class instance

        Args:
            dictionary: values for class update method saved as dictionary
        """

        if cls.__name__ == "Square":
            tmp_obj = cls(1)
        else:
            tmp_obj = cls(1, 1)

        tmp_obj.update(**dictionary)

        return tmp_obj
