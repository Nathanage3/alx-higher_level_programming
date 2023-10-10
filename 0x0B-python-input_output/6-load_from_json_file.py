#!/usr/bin/python3
"""This is a module to save decoded json
    file to an other file"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Parameters:
    - filename: The name of the JSON file.

    Returns:
    - Object: Python data structure represented by the JSON string in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
