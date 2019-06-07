#!/usr/bin/python3
"""Module for append_write"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and
       returns number of characters added
    """
    with open(filename, 'a') as f:
        append = f.write(text)
    return (append)
