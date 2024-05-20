#!/usr/bin/python3

"""defines the class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines Rectangle based on BaseGeometry"""
    def __init__(self, width, height):
        """instantiates with width and height

        Args:
            width: horizontal side length
            height: vertical side length
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
