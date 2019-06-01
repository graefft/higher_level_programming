#!/usr/bin/python3
"""Module for multiplying 2 matrices using NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function to multiply 2 matrices using NumPy"""
    result = np.dot(m_a, m_b)
    return (result)
