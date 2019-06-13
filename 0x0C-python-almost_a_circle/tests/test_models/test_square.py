#!/usr/bin/python3
'''This module is for Square class tests'''


import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    '''Tests for the Square class'''


    @classmethod
    def setUpClass(cls):
        '''initializes class'''
