#!/usr/bin/python3
"""Module for text_indentation method"""


def text_indentation(text):
    """Function that prints text with 2 new lines after . ? and :"""
    if type(text) is not str:
        raise TypeError('text must be a string')

    string = ''

    for i in (text):
        if i == '.' or i == '?' or i == ':':
            string += i
            print(string.strip(' '), end='\n\n')
            string = ''
        else:
            string += i
        print(string.strip(' '), end='')
