#!/usr/bin/python3
"""Define integer addition function."""


def add_integer(a, b=98):
    """
    Adds two numbers together

    Args:
    a: The first parameter, must be an integer or float.
    b: The second parameter (default is 98), must be an integer or float.

    Returns:
    The sum of a and b, casted to an integer.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
