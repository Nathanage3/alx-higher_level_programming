#!/usr/bin/python3
"""This is a module to save JSON serialized
    or decoded file to an other file."""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Parameters:
    - my_obj: The object to be written to the file in JSON format.
    - filename: The name of the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
