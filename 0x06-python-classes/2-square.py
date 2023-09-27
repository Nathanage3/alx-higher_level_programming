#!/usr/bin/python3
'''Defining the class Square'''


class Square:
    '''Represent the Square'''


    def __init__(self, size=0):
        '''initialize the Square

        Args:
        size(int): the size of Square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
