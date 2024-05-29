#!/usr/bin/python3

"""Unittests for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """defines unittests for methods in Rectangle class"""
    def test_init_wh(self):
        """test width, height"""
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

    # def test_init_wh(self):
    #     """test width, height"""
    #     r = Rectangle(1, 2)
    #     self.assertEqual(r.width, 1)
    #     self.assertEqual(r.height, 2)
    #
    # def test_init_whx(self):
    #     """test width, height, x"""
    #     r = Rectangle(1, 2, 3)
    #     self.assertEqual(r.width, 1)
    #     self.assertEqual(r.height, 2)
    #     self.assertEqual(r.x, 3)
    #
    # def test_init_whxy(self):
    #     """test width, height, x, y"""
    #     r = Rectangle(1, 2, 3, 4)
    #     self.assertEqual(r.width, 1)
    #     self.assertEqual(r.height, 2)
    #     self.assertEqual(r.x, 3)
    #     self.assertEqual(r.y, 4)
