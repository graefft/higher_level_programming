#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
        """Max integer tests"""

        def test_normal(self):
            """Test normal case"""
            self.assertEqual(max_integer([1, 2, 3, 4], 4))

        def test_one(self):
            """Test one int"""
            self.assertEqual(max_integer([3], 1))

        def test_empty(self):
            """Test empty list"""
            self.assertEqual(max_integer(), None)

        def test_same(self):
            """Test same ints"""
            self.assertEqual(max_integer([21, 21, 21, 21], 4))

        def test_string(self):
            """Test with string"""
            self.assertEqual(max_integer(["Hi", 2, 3, 4], 4))

        def test_float(self):
            """Test with float"""
            self.assertEqual(max_integer([1, 2, 3, 4.4], 4))

        def test_negative(self):
            """Test negative int"""
            self.assertEqual(max_integer([-1, -2, -3, -4]. 4))

        def test_large(self):
            """Test large numbers"""
            self.assertEqual(max_integer([99999, 999999, 99999999], 9999999))


if __name__ == '__main__':
    unittest.main()
