#!/usr/bin/python3
"""This is a module for inverting an incoming
    attribute"""


class MyInt(int):
    """Define a class MyInt"""
    def __eq__(self, num):
        """Define an equal to method

            Args:
                num (int): the number passed to MyInt class
            Returns:
                An inverted number value.
        """
        return super().__ne__(num)

    def __ne__(self, num):
        """Define a method for returning equal to.

            Args:
            num (int): the number from MyInt

            Returns:
                An equal to value which is inverse
        """
        return super().__eq__(num)
