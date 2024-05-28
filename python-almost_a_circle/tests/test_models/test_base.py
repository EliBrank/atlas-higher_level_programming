#!/usr/bin/python3

"""Unittests for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """defines unittests for methods in Base class"""

    def test_init_id(self):
        """test id"""
        obj_1 = Base()
        self.assertTrue(obj_1.id)
        self.assertEqual(obj_1.id, 1)
        obj_2 = Base()
        self.assertEqual(obj_2.id, 2)
        obj_3 = Base(20)
        self.assertEqual(obj_3.id, 20)
        obj_4 = Base()
        self.assertEqual(obj_4.id, 3)

    # def test_
