#!/usr/bin/python3
"""Unittest for Base module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class Testbase_instances(unittest.TestCase):
    """Type class of testing for instances"""

    def test_None(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_empty(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id -1)

    def test_single_id(self):
        self.assertEqual(5, Base(5).id)

    def test_public_id(self):
        public_b = Base(5)
        public_b.id = 10
        self.assertEqual(10, public_b.id)

    def test_private_ins(self):
        with self.assertRaises(AttributeError):
            print(Base(5).__nb_instances)

    def test_str(self):
        self.assertEqual("tequila", Base("tequila").id)

    def test_float(self):
        self.assertEqual(3.1, Base(3.1).id)

    def test_dict(self):
        self.assertEqual({"val1": 1, "val2": 2}, Base({"val1": 1, "val2": 2}).id)

    def test_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_twoarg(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_set(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozen(self):
        self.assertEqual(frozenset({"a", "b", "c"}), Base(frozenset({"a", "b", "c"})).id)


class Testbase_to_json(unittest.TestCase):
    """Type class of testing for to_json"""


    def test_to_json_none(self):
        self.assertEqual('[]', Base.to_json_string(None))

    def test_to_json_empty(self):
        self.assertEqual('[]', Base.to_json_string([]))

    def test_to_json_TE(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_TE2(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 10)

    def test_to_json_typeR(self):
        rec = Rectangle(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))

    def test_to_json_typeS(self):
        sqr = Square(10, 2, 1)
        self.assertEqual(str, type(Base.to_json_string([sqr.to_dictionary()])))

    def test_to_json_dictR(self):
        rec = Rectangle(10, 7, 2, 8)
        self.assertTrue(len(Base.to_json_string([rec.to_dictionary()])))

    def test_to_json_dictS(self):
        sqr = Square(10, 2, 1)
        self.assertTrue(len(Base.to_json_string([sqr.to_dictionary()])))

    def test_to_json_dictRx2(self):
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(2, 4, 6)
        list_dicts = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)))

    def test_to_json_dictSx2(self):
        sqr1 = Square(10, 2, 1)
        sqr2 = Square(7, 9)
        list_dicts = [sqr1.to_dictionary(), sqr2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)))

class Testbase_from_json(unittest.TestCase):
    """Type class unittest from json method"""


    def test_from_json_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_TE(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_TE2(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 10)

    def test_from_json_type(self):
        linput = [{"id": 89, "width": 10, "height": 4}]
        json_linput = Rectangle.to_json_string(linput)
        loutput = Rectangle.from_json_string(json_linput)
        self.assertEqual(list, type(loutput))

    def test_from_json_dictR(self):
        linput = [{"id": 89, "width": 10, "height": 4, "x": 2}]
        json_linput = Rectangle.to_json_string(linput)
        loutput = Rectangle.from_json_string(json_linput)
        self.assertEqual(linput, loutput)

    def test_from_json_dictS(self):
        linput = [{"id": 89, "size": 10, "height": 4}]
        json_linput = Square.to_json_string(linput)
        loutput = Square.from_json_string(json_linput)
        self.assertEqual(linput, loutput)

    def test_from_json_dictRx2(self):
        linput = [{"id": 89, "width": 10, "height": 4, "x": 2, "y": 1},
                  {"id": 7, "width": 1, "height": 7, "x": 8, "y": 2}
        ]
        json_linput = Rectangle.to_json_string(linput)
        loutput = Rectangle.from_json_string(json_linput)
        self.assertEqual(linput, loutput)

    def test_from_json_dictSx2(self):
        linput = [{"id": 89, "width": 10, "height": 4, "x": 2, "y": 1},
                  {"id": 7, "width": 1, "height": 7, "x": 8, "y": 2}
        ]
        json_linput = Square.to_json_string(linput)
        loutput = Square.from_json_string(json_linput)
        self.assertEqual(linput, loutput)


class Testbase_save_file(unittest.TestCase):
    """Type class unittest from save_to_file method"""

    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_file_TE(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_file_TE2(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 10)

    def test_save_file_rec(self):
        rec = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()))

    def test_save_file_sqr(self):
        sqr = Square(10, 2, 1)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()))

    def test_save_file_recx2(self):
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(7, 2, 1, 4, 6)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()))

    def test_save_file_sqrx2(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(10, 2, 1,)
        Square.save_to_file([sqr1, sqr2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()))

    def test_save_file_cls(self):
        rec = Rectangle(10, 2, 1)
        Base.save_to_file([rec])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()))

    def test_save_file_rw(self):
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file([sqr])
        sqr = Square(80, 10, 4, 2)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()))


class Testbase_load_file(unittest.TestCase):
    """Type class unittest from load_to_file method"""

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_file_empty(self):
        load = Rectangle.load_from_file()
        self.assertEqual([], load)

    def test_load_file_TE(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 10)

    def test_load_file_rec(self):
        rec = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rec])
        load = Rectangle.load_from_file()
        self.assertEqual(str(rec), str(load[0]))

    def test_load_file_sqr(self):
        sqr = Square(10, 2, 1)
        Square.save_to_file([sqr])
        load = Square.load_from_file()
        self.assertEqual(str(sqr), str(load[0]))

    def test_load_file__type_rec(self):
        rec = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rec])
        load = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in load))

    def test_load_file_type_sqr(self):
        sqr = Square(10, 2, 1)
        Square.save_to_file([sqr])
        load = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in load))

    def test_load_file_reccp1(self):
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(10, 2, 1, 4, 6)
        Rectangle.save_to_file([rec1, rec2])
        load = Rectangle.load_from_file()
        self.assertEqual(str(rec1), str(load[0]))

    def test_load_file_reccpp2(self):
        rec1 = Rectangle(10, 7, 2, 8, 3)
        rec2 = Rectangle(10, 2, 1, 4)
        Rectangle.save_to_file([rec1, rec2])
        load = Rectangle.load_from_file()
        self.assertEqual(str(rec2), str(load[1]))

    def test_load_file_sqrcp1(self):
        sqr1 = Square(10, 2, 1)
        sqr2 = Square(10, 7, 2, 8)
        Square.save_to_file([sqr1, sqr2])
        load = Square.load_from_file()
        self.assertEqual(str(sqr1), str(load[0]))

    def test_load_file_sqrcp2(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(10, 2, 1)
        Square.save_to_file([sqr1, sqr2])
        load = Square.load_from_file()
        self.assertEqual(str(sqr2), str(load[1]))


class Testbase_create(unittest.TestCase):
    """Type class unittest from create method"""

    def test_create_isNot(self):
        rec = Rectangle(10, 7, 2, 8)
        rec_dict = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_dict)
        self.assertIsNot(rec, rec2)

    def test_create_rec(self):
        rec = Rectangle(10, 7, 2, 8)
        rec_dict = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_dict)
        self.assertEqual("[Rectangle] (3) 2/8 - 10/7", str(rec))

    def test_create_rec2(self):
        rec = Rectangle(89, 10, 7, 4)
        rec_dict = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_dict)
        self.assertEqual("[Rectangle] (5) 7/4 - 89/10", str(rec2))

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

if __name__ == '__main__':
    unittest.main()
