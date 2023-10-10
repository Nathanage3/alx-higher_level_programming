#!/usr/bin/python3
""" A module for using JSON conding."""


import json

def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    Parameters:
    - my_obj: Object to be serialized to JSON.

    Returns:
    - str: JSON representation of the object.
    """
    return json.dumps(my_obj)
