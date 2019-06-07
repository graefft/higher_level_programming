#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of Student"""
        if type(attrs) is not list:
            return (self.__dict__)
        else:
            for i in attrs:
                if type(i) is not str:
                    return (self.__dict__)
        new_dict = {}
        for i in attrs:
            if i in self.__dict__:
                new_dict[i] = self.__dict__.get(i)
        return new_dict
