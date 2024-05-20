#!/usr/bin/python3

import json

"""defines the function to_json_string"""


def to_json_string(my_obj):
    """converts python object to json string

    Returns: json string, if possible
    """

    return json.dumps(my_obj)
