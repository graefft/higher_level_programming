#!/usr/bin/python3
"""Module for text_indentation method"""


def text_indentation(text):
    """Function that prints text with 2 new lines after . ? and :"""
    if type(text) is not str:
        raise TypeError('text must be a string')

    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{}".format(text[i]), end='\n\n')
        else:
            print("{}".format(text[i]), end='')
