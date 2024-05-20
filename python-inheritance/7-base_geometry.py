#!/usr/bin/python3

"""defines the class BaseGeometry"""


class BaseGeometry:
    """defines empty area method"""

    def area(self):
        """only raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks that value passed is integer and greater than zero

        Returns: exception if value is non-integer or <= zero
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
