#!/usr/bin/python3
"""
    Defines a student class
"""


class Student:
    """
        Defines a student class
    """

    def __init__(self, first_name, last_name, age):
        """
            Initializing instance variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Retrieves the dict reprenting the class
        """
        return (self.__dict__)
