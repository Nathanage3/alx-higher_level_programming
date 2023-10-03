#!/usr/bin/python3
"""Define a function that prints a square matrix."""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
    size: The size length of the square.

    Raises:
    TypeError: If size is not an integer or if size is a float less than 0.
    ValueError: If size is less than 0.
    """

    # Type checking for size
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    # Value checking for size
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print("#" * size)
