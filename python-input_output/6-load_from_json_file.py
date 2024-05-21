#!/usr/bin/python3

"""defines the function load_from_json_file"""

import json


def load_from_json_file(filename):
    """converts json file contents to python object"""

    with open(filename, "r") as f:
        return json.load(f)
