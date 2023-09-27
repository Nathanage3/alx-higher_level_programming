#!/usr/bin/python3
'''Define the class Square'''


class Square:
    '''Represent Square'''


    def __init__(self, size=0):
        '''initialize the Square


        Args:
        size(int): the size of Squarw
        '''
        self.size = size

    @property
    def size(self):
        '''return the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''return the size '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return size'''
        return self.__size * self.__size
