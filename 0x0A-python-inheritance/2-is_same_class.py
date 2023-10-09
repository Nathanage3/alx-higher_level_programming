#!/usr/bin/python3
"""Module has a functction that checks if an object is an instance
or a specified class
"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an
        instance of the specified class ; otherwise False
    Args:
        obj (obj): the object to check
        a_class (obj): The class to check against
    Returns:
        bool: if isinstance othewise false
    """

    return True if type(obj) is a_class else False
