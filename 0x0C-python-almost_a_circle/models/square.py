#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id_=None):
        """the Square class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """square"""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter square"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates square"""
        attribute_names = ['id', 'size', 'x', 'y']
        if args:
            for i, val in enumerate(args):
                if i < 4:
                    setattr(self, attribute_names[i], val)
            return
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def to_dictionary(self):
        """Converts the square object to a dictionary"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
