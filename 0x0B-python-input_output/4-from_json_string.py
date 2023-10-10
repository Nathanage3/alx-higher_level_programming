#!/usr/bin/python3
"""This module is JSON decoder"""


import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Parameters:
    - my_str: JSON string to be deserialized to a Python object.

    Returns:
    - Object: Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
