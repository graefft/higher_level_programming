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
        cls.s1 = Square(10)
        cls.s2 = Square(2)
        cls.s3 = Square(10, 0, 0, 12)
        cls.s4 = Square(10, 2, 4, 5)

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

    def test_square_id(self):
        '''test Square ids'''
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 12)

    def test_square_size(self):
        '''test Square size'''
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 10)

if __name__ == '__main__':
    unittest.main()
