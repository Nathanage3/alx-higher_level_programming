#!/usr/bin/python3
"""
Contains a class MyList that inherits from list builtin
"""


class MyList(list):
    """Inherits from the list class"""

    def __init__(self):
        """Initializes the object
        """
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list
        """
        print(sorted(self))
