#!/usr/bin/python3
'''Define class Square'''


class Square:
'''represent class Square'''


    def __init__(self, size=0, position=(0, 0)):
        '''initialize Square


        Args:
        size(int): the size of square
        positio(int): the position of size
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''return size'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''return size'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Return the area'''
        return self.__size * self.__size

    def my_print(self):
        '''return nothing'''
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
