#!/usr/bin/python3
"""that defines a square"""


class Square:
    """ only squares integers """

    def __init__(self, size=0):
        """ Exeptions to not integers """
        if int(size) > -1 and size == int(size):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
            raise ValueError("size must be >= 0")
