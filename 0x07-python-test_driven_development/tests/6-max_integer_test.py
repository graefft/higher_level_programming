#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
        """Max integer tests"""

        def test_normal(self):
            """Test normal case"""
            self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        def test_out_of_order(self):
            """Test if out of order"""
            self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        def test_one(self):
            """Test one int"""
            self.assertEqual(max_integer([3]), 3)

        def test_empty(self):
            """Test empty list"""
            self.assertEqual(max_integer([]), None)

        def test_same(self):
            """Test same ints"""
            self.assertEqual(max_integer([21, 21, 21, 21]), 21)

        def test_string(self):
            """Test with string"""
            mix = ["Hi", 2, 3, 4]
            self.assertRaises(TypeError, max_integer, mix)

        def test_float(self):
            """Test with float"""
            self.assertEqual(max_integer([1, 2, 3, 4.4]), 4.4)

        def test_negative(self):
            """Test negative int"""
            self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        def test_none(self):
            """Test none parameter"""
            self.assertRaises(TypeError, max_integer, None)

        def test_noparam(self):
            """Test no parameter"""
            self.assertRaises(TypeError, max_integer, 0)

        def test_multiple_string(self):
            """Tests multiple strings"""
            self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

if __name__ == '__main__':
    unittest.main()
