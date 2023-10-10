#!/usr/bin/python3
"""returns the dictionary description with
simple data structure (list, dictionary,
string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """returns the dictionary description with
    simple data structure (list, dictionary,
    string, integer and boolean)
    for JSON serialization of an object
    """
    return obj.__dict__
