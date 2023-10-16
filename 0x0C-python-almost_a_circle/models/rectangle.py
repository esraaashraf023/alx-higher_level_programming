#!/usr/bin/python3
"""Module for Rectangle class"""
from models.rectangle import Base

class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """hight of rextangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

     @property
     def y(self):
         """Y of rextangle"""
         return self.__y

      @y.setter
      def y(self, value):
          self.__y = value

       @property
       def def x(self):
         """x of rextangle"""
         return self.__x
     
        @x.setter
      def x(self, value):
          self.__x = value 
