#!/usr/bin/python3

"""defines the function from_json_string"""

import json


def from_json_string(my_str):
    """converts json string to python object

    Returns: python object, if possible
    """

    return json.loads(my_str)
