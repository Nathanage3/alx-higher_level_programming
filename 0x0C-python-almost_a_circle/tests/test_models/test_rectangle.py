#!/bin/usr/python3
"""Unittest for Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class Testrec_instances(unittest.TestCase):
    """Type class unittest instance for rectangle"""

    def test_isrec(self):
        self.assertIsInstance(Rectangle(10, 7), Base)

    def test_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_w_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__width)

    def test_w_getter(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        self.assertEqual(10, rec.width)

    def test_w_setter(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_h_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__height)

    def test_h_getter(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        self.assertEqual(7, rec.height)

    def test_h_setter(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_y_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__y)

    def test_y_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.y)

    def test_y_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.y = 10
        self.assertEqual(10, rec.y)

    def test_x_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__x)

    def test_x_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.x)

    def test_x_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_single_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_two_arg(self):
        rec = Rectangle(10, 7)
        rec2 = Rectangle(4, 8)
        self.assertNotEqual(rec.id, rec2.id)

    def test_three_arg(self):
        rec = Rectangle(10, 7, 2)
        rec2 = Rectangle(4, 8, 1)
        self.assertNotEqual(rec.id, rec2.id)

    def test_four_arg(self):
        rec = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(4, 2, 1, 3)
        self.assertNotEqual(rec.id, rec2.id)

    def test_five_arg(self):
        rec = Rectangle(10, 7, 2, 8, 4)
        rec2 = Rectangle(4, 2, 1, 3, 7)
        self.assertNotEqual(rec.id, rec2.id)

    def test_six_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 7, 2, 8, 4, 1)

class Testrec_w(unittest.TestCase):
    """Type class unittest instance for rectangle"""

    def test_w_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)

    def test_w_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Edward", 10)

    def test_w_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.2, 7)

    def test_w_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 10, "b": 7}, 8)

    def test_w_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([10, 7, 8], 8)

    def test_w_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((10, 7, 8), 8)

    def test_w_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 10)

    def test_w_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 10)

    def test_w_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({10, 7, 8}, 8)

    def test_w_frozen(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({10, 7, 8, 1}), 8)

    def test_w_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 7)

    def test_w_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 7)


if __name__ == '__main__':
    unittest.main()
