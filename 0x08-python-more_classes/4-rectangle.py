#!/usr/bin/python3
"""Define a rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
        width (int): the width of rectangle.
        height (int): the height of a rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of a rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set a height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the area."""
        return self.width * self.height

    def perimeter(self):
        """Get the perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Initialize a string."""
        if self.width == 0 or self.height == 0:
            return ""
        rows = []
        rows = (("#" * self.width) + "\n") * self.height
        return rows[:-1]
    def __repr__(self):
        """Initialize represetation for developer readable."""
        return f"Rectangle({self.width}, {self.height})"
