#!/usr/bin/python3
"""This module is for the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class to inherit from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns size of Square"""
        return (self.width)

    @size.setter
    def size(self, size):
        """setter for size of Square"""
        self.width = size
        self.height = size

    def __str__(self):
        """override __str__ method"""
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width))
