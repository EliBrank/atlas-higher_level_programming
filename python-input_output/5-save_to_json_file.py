#!/usr/bin/python3

"""defines the function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """converts/writes python object to json file"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
