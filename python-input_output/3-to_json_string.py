#!/usr/bin/python3

"""defines the function to_json_string"""

import json


def to_json_string(my_obj):
    """converts python object to json string

    Returns: json string, if possible
    """

    return json.dumps(my_obj)
