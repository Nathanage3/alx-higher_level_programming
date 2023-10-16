#!/bin/usr/python3
"""Unittest for Square"""

import unittest
from models.base import Base
from models.square import Square

class Testsqr_instances(unittest.TestCase):
    """Type class unittest instance for rectangle"""

    def test_issqr(self):
        self.assertIsInstance(Square(10, 7), Base)

    def test_empty(self):
        with self.assertRaises(TypeError):
            Square()

    def test_issqr2(self):
        self.assertIsInstance(Square(10), Square)


    def test_h_priv(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 7, 8, 2).__size)

    def test_sz_getter(self):
        self.assertEqual(10, Square(10, 7, 8, 4).size)

    def test_s_setter(self):
        sqr = Square(10, 7, 8, 2)
        sqr.size = 10
        self.assertEqual(10, sqr.size)

    def test_h_getter(self):
        sqr = Square(10, 7, 8, 2)
        sqr.size = 10
        self.assertEqual(10, sqr.height)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_two_arg(self):
        sqr = Square(10, 7)
        sqr2 = Square(4, 8)
        self.assertNotEqual(sqr.id, sqr2.id)

    def test_three_arg(self):
        sqr = Square(10, 7, 2)
        sqr2 = Square(4, 8, 1)
        self.assertNotEqual(sqr.id, sqr2.id)

    def test_four_arg(self):
        sqr = Square(10, 7, 2, 8)
        sqr2 = Square(4, 2, 1, 3)
        self.assertNotEqual(sqr.id, sqr2.id)

    def test_six_arg(self):
        with self.assertRaises(TypeError):
            Square(10, 7, 2, 8, 4, 1)

class Testsqr_w(unittest.TestCase):
    """Type class unittest instance for rectangle"""

    def test_s_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 10)

    def test_s_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Edward", 10)

    def test_s_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10.2, 7)

    def test_s_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 10, "b": 7}, 8)

    def test_s_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([10, 7, 8], 8)

    def test_s_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((10, 7, 8), 8)

    def test_s_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 10)

    def test_s_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 10)

    def test_s_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({10, 7, 8}, 8)

    def test_w_frozen(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({10, 7, 8, 1}), 8)

    def test_s_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10, 7)

    def test_s_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 7)
