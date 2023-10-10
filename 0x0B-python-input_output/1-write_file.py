#!/usr/bin/python3
"""Contains function that writes a
string to a text file (UTF8)
and returns the number of character
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        count = file.write(text)

    return count
