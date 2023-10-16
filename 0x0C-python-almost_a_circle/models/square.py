#!/usr/bin/python3
"""Module of Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Type class square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ function"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size function public"""

        return self.width

    @size.setter
    def size(self, value):
        """size function for setter"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update function"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = k
                elif j == "size":
                    self.size = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def __str__(self):
        """__str__ function"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """to_dictionary function"""

        return {
            "id": self.id, "size": self.width, "x": self.x, "y": self.y
        }
