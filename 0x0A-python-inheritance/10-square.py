#!/usr/bin/python3
"""Module for Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from 'Rectangle'"""
    def __init__(self, size):
        """Instantiation with private size attribute"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
