#!/usr/bin/python3
"""Module of rectangle"""


from models.base import Base


class Rectangle(Base):
    """Type class of a rectangle inherited from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width function private"""

        return self.__width

    @width.setter
    def width(self, value):
        """width function for setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height function private"""

        return self.__height

    @height.setter
    def height(self, value):
        """height function private"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x function private"""

        return self.__x

    @x.setter
    def x(self, value):
        """x function setter"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y function private"""

        return self.__y

    @y.setter
    def y(self, value):
        """y function setter"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """areat function"""

        return self.width * self.height

    def display(self):
        """display function"""

        [print("") for y in range(self.y)]
        for j in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for k in range(self.width)]
            print("")

    def __str__(self):
        """str function"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """update function"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = k
                elif j == "width":
                    self.width = k
                elif j == "height":
                    self.height = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def to_dictionary(self):
        """to_dictionary function"""

        return {
            "id": self.id, "width": self.width, "height": self.height,
            "x": self.x,
            "y": self.y,
        }
