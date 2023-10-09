#!/usr/bin/python3
"""Module that holds the class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes the class
            Args:
                width (int): width rectangle
                height (int): height rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
