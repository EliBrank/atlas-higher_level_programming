#!/usr/bin/python3

"""Unittests for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """defines unittests for methods in Rectangle class"""
    def test_init(self):
        """test width, height, id"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 2, 3, 4, 12)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.id, 12)
