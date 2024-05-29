#!/usr/bin/python3

"""Unittests for Square class"""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """defines unittests for methods in Square class"""
    def test_init(self):
        """test size, x, y"""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)

        s2 = Square(1, 2)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)

        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.size, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)
        self.assertEqual(s4.id, 4)


    def test_init_NaN(self):
        """test non-nums for Square init"""
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_init_negative(self):
        """test negative nums for Square init"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_init_wh_zero(self):
        """test zero for size"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_update(self):
        """test update method on existing object"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 1)

        s1.update(89)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 89)

        s1.update(89, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 89)

        s1.update(89, 2, 3)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 89)

        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 89)


    def test_update_kwargs(self):
        """test update method using kwargs as input"""
        s1 = Square(10, 10, 10, 1)

        s1.update(**{ 'id': 89 })
        self.assertEqual(s1.id, 89)

        s1.update(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

        s1.update(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

        s1.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_create(self):
        """test create method with different numbers of args"""
        s1 = Square.create(**{ 'id': 89 })
        self.assertEqual(s1.id, 89)

        s2 = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s2.id, 89)
        self.assertEqual(s2.size, 1)

        s3 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s3.id, 89)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)

        s4 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s4.id, 89)
        self.assertEqual(s4.size, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)
