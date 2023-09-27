#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Simple class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with the given size and position

        Args:
            size (int): Size of the square
            position (tuple): Locate the position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the current size with some constrains"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position size with some constrains"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Compute the area of the square

        Return:
            int: current square area
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character `#`"""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        [
            print(" " * self.__position[0] + "#" * self.__size)
            for _ in range(self.__size)
        ]
