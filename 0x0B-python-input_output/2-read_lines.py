#!/usr/bin/python3
"""Module for number_of_lines"""


def number_of_lines(filename=""):
    """Returns number of lines in a text file"""
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
        return (count)


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file and prints to stdout"""
    line_count = 0
    line_number = number_of_lines(filename)
    with open(filename, 'r') as f:
        if nb_lines <= 0 or nb_lines >= line_number:
            print(f.read(), end='')
        else:
            for line in f:
                if line_count == nb_lines:
                    break
                line_count += 1
                print(line, end='')
