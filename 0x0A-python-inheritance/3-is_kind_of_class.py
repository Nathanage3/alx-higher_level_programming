#!/usr/bin/python3

"""Module checks if an object is an instance of a
class or of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Function returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class ;
    otherwise False
    Args:
        obj (obj): the object to check
        a_class (obj): The class to check against
    Returns:
        bool: if isinstance othewise false
    """

    return True if isinstance(obj, a_class) else False
