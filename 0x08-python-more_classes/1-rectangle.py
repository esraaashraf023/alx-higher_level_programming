#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """A class Rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle instance with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
