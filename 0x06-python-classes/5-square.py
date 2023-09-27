#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Simple class representing a square"""
    def __init__(self, size=0):
        """
        Initialize a square with the given size

        Args:
            size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the Square instance."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the Square instance."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Compute the area of the square

        Return:
            int: current square area
        """
        return self.__size ** 2

    def my_print(self):
        """prints the character `#`"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
