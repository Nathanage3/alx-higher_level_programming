#!/usr/bin/python3
'''Define class Square'''


class Square:
    '''Initialize the Square'''


    def __init__(self, size=0):
        '''initialilze the Square


        Args:
        size(int): the size of Square
        '''
        self.size = size
    def size(self):
        '''return size'''
        return self.__size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        '''return size'''
        return self.__size * self__size
