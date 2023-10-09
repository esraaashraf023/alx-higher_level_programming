#!/usr/bin/python3
"""Module for `Square` class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a Square"""

    def __init__(self, size):
        """Initializing `Square` shape"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Implement area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Official string format for the Square"""
        return f"[Square] {self.__size}/{self.__size}"
