#!/usr/bin/python3
"""Module that holds the class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle but makes a square
    """

    def __init__(self, size):
        """Initializes a square
            Args:
                size (int): size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
