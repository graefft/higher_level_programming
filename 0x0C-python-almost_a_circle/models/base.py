#!/usr/bin/python3
"""Module for Base Class"""


import json


class Base():
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        return (json.dumps(list_dictionaries))

