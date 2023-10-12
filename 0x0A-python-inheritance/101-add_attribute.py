#!/usr/bin/python3
"""This is a module that add an attribute"""


def add_attribute(obj, name, value):
    """A method that check  obj has attribute.

    Args:
        obj: the object to add attributie
        name (str): the name attribute
        value: the value attribute

    Returns:
        The attribute of the method
    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
