#!/usr/bin/python3
""" Module that returns a list of available
    attributes and methods of an object:
"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object
    Args:
        obj(obj) - the object to check
    Returns:
        list: list of every attributes and methods
    """

    return dir(obj)
