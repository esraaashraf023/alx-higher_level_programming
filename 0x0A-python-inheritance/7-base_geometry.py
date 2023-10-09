#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A base class"""

    def area(self):
        """The geometric shape"""
        raise Exception("This area has not been implemented yet")

    def integer_validator(self, name, value):
        """validate a value as an integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
