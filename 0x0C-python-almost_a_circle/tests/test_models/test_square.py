#!/usr/bin/python3
'''This module is for Square class tests'''


import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Tests for the Square class'''

    @classmethod
    def setUpClass(cls):
        '''initializes class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''tears down test'''
        pass

    def test_square_class_type(self):
        '''test class type'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_square_inheritance(self):
        '''test inheritance of Rectangle'''
        self.assertTrue(issubclass(Square, Rectangle))
