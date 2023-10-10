#!/usr/bin/python3
"""This is a module for opening file."""

def read_file(filename=""):
    """Read the contents of the given file and print them to stdout.
    Args:
        filename(str): the filename
    """

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="");
