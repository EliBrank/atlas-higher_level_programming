#!/usr/bin/python3

"""Unittests for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """defines unittests for methods in Rectangle class"""
    def test_init(self):
        """test width, height, x, y"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)


    def test_init_NaN(self):
        """test non-nums for Rectangle init"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_init_negative(self):
        """test negative nums for Rectangle init"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_init_wh_zero(self):
        """test zero for width and height"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_update(self):
        """test update method on existing object"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

        r1.update(89)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 89)

# update() in Rectangle
#
# update(89) in Rectangle
#
# update(89, 1) in Rectangle
#
# update(89, 1, 2) in Rectangle
#
# update(89, 1, 2, 3) in Rectangle
#
# update(89, 1, 2, 3, 4) in Rectangle
#

# area()
#
# __str__() for Rectangle
#
# display() without x and y
#
# display() without y
#
# display()
#
# to_dictionary() in Rectangle
#
# update(**{ 'id': 89 }) in Rectangle
#
# update(**{ 'id': 89, 'width': 1 }) in Rectangle
#
# update(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle
#
# update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle
#
# update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle
#
# Rectangle.create(**{ 'id': 89 }) in Rectangle
#
# Rectangle.create(**{ 'id': 89, 'width': 1 }) in Rectangle
#
# Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle
#
# Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle
#
# Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle
#
# Rectangle.save_to_file(None) in Rectangle
#
# Rectangle.save_to_file([]) in Rectangle
#
# Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle
#
# Rectangle.load_from_file() when file doesn’t exist
#
# Rectangle.load_from_file()
