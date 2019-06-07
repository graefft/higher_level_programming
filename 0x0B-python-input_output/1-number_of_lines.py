#!/usr/bin/python3
"""Module for number_of_lines"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file"""
    count = 0
    with open(filename, 'r', encoding="utf-8") as read_data:
        for line in read_data:
            count += 1
        return (count)
