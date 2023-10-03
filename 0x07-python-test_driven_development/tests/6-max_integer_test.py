#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This is the class unittest for the max integer function
    """

    def test_sorted_list(self):

       sorted_list = [1, 2, 3, 4]
       self.assertEqual(max_integer(sorted_list), 4)

    def test_unsorted_list(self):

        unsorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(unsorted_list), 4)

    def test_empty_list(self):

        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floatl(self):

        floatl = [1.25, 2.33, 3.67, 4.44]
        self.assertEqual(max_integer(floatl), 4.44)

    def test_intl_floatl(self):

        intl_floatl = [1.25, 4.44, 4, 5]
        self.assertEqual(max_integer(intl_floatl), 5)

    def test_only_one(self):

        only_one = [7]
        self.assertEqual(max_integer(only_one), 7)

    def test_max_first(self):

        max_first = [4, 1, 2, 3]
        self.assertEqual(max_integer(max_first), 4)

    def test_max_middle(self):

        max_middle = [1, 2, 4, 3]
        self.assertEqual(max_integer(max_middle), 4)

    def test_non_string(self):

        self.assertEqual(max_integer(""), None)

    def test_many_strings(self):

        many_strings = ["string1", "string2", "string3"]
        self.assertEqual(max_integer(many_strings), "string3")

if __name__ == '__main__':
    unittest.main()
