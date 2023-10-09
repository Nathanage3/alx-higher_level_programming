#!/usr/bin/python3
"""Module holds a function that determines if an object is an instance of a
class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False.
    Args:
        obj (obj): the object to check
        a_class (obj): The class to check against
    Returns:
        bool: if isinstance othewise false
    """

    return True if isinstance(obj, a_class) and \
        type(obj) is not a_class else False
