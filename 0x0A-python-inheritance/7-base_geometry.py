#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A base class for geometric shapes"""

    def area(self):
        """Calculates the area of the geometric shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a value as an integer"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
