#!/usr/bin/python3
"""This module is to replace a string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file, after each line containing a
    specific string.

    Args:
        filename (str): The name of the file to be modified.
        search_string (str): The string to search for in the file.
        new_string (str): The string to insert after lines containing
                          the search string.

    Returns:
        None
    """
    # Read the file into memory
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Append the new_string after lines containing the search_string
    i = 0
    while i < len(lines):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)
            i += 1  # Skip the newly added line
        i += 1

    # Write the modified lines back to the file
    with open(filename, 'w') as f:
        f.writelines(lines)
