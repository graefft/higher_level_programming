#!/usr/bin/python3
"""Module for from_json_string(my_str)"""


import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
       represented as a JSON string
    """
    return (json.loads(my_str))
