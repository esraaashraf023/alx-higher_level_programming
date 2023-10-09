#!/usr/bin/python3
"""Module for `Rectangle` class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle"""
    def __init__(self, width, height):
        """Initializing `Rectangle` shape

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
