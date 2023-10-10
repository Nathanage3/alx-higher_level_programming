#!/usr/bin/python3
"""It has a module tha append an other file
    to a previously stated file.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF-8) and
    return the number of characters added.

    Parameters:
    - filename (str): The name of the file.
    - text (str): The text to append to the file.

    Returns:
    - int: Number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
