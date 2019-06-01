#!/usr/bin/python3
"""Module for Matrix Multiplication program"""


def matrix_mul(m_a, m_b):
    """Function to multiply two matrices"""
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    for x in m_a:
        if type(x) is not list:
            raise TypeError('m_a must be a list of lists')
    for x in m_b:
        if type(x) is not list:
            raise TypeError('m_b must be a list of lists')
    if m_a == 0 or m_a is None or m_a == [[]] or (len(m_a) == 0):
        raise ValueError('m_a can\'t be empty')
    if m_b == 0 or m_b is None or m_b == [[]] or (len(m_b) == 0):
        raise ValueError('m_b can\'t be empty')

    for row in m_a:
        if len(m_a[0]) != len(row):
            raise TypeError('each row of m_a must should be of the same size')
    for row in m_b:
        if len(m_b[0]) != len(row):
            raise TypeError('each row of m_b must should be of the same size')

    for row in m_a:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return (result)
