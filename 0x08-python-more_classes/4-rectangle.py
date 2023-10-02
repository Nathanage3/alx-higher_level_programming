#!/usr/bin/python3
"""Define a rectangle class."""


class Rectangle:
    """Represent a rectangle class."""


    def __init__(self, width=0, height=0):
        """Initialize a rectangle class.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.

            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width."""
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
        """Get/set the height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            return rows = (("#" * self.width))

    def __repr__(self):
        """Return a formal representation of the rectanle."""
        return f"Rectangle({self.width}, {self.heigiht})"
