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

    def to_json(self, attrs=None):
        """
            Retrieves the dict reprenting the class
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return my_dict
