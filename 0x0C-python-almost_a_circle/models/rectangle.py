#!/usr/bin/python3
"""This module creates class Rectangle"""


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """private attribute getter for width"""
        return (self.__width)

    @property
    def height(self):
        """private attribute getter for height"""
        return (self.__height)

    @property
    def x(self):
        """private attribute getter for x"""
        return (self.__x)

    @property
    def y(self):
        """private attribute getter for y"""
        return (self.__y)

    @width.setter
    def width(self, width):
        """setter for width"""
        self.__width = width

    @height.setter
    def height(self, height):
        """setter for height"""
        self.__height = height

    @x.setter
    def x(self, x):
        """setter for x"""
        self.__x = x

    @y.setter
    def y(self, y):
        """setter for y"""
        self.__y = y
