#!/usr/bin/python3
"""Define a rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
        width (int): the width of rectangle.
        height (int): the height of a rectangle.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Initialize a string."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return ((symbol * self.width + "\n") * self.height).rstrip()

    def __repr__(self):
        """Return a formal representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger or equal rectangle."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new rectangle instance with width and height are equal"""
        return cls(size, size)
