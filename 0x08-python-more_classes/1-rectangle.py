#!/usr/bin/pythonn3
'''Defines a Rectangle class.'''


class Rectangle:
    """class Rectangle is started."""


    def __init__(self, width=0, height=0):
        '''Initializing Class.

        Args:
            width (int): the width of rectangle.
            height (int): the height of the rectaangle.

            '''
        self.width = width
        self.height = height


    @property
    def width(self):
        '''Get/set the width of the rectangle'''
        return self.__width


    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def  height(self, value):
        '''Get/set the height of the rectangle.'''
        return self.__height


    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
