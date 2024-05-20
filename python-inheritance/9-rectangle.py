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

    def area(self):
        """calculates Rectangle area based on width and height

        Returns: area, i.e. width multiplied by height
        """

        return self.__width * self.__height

    def __str__(self):
        """formats print output to display width and height

        Returns: "[Rectangle] <width>/<height>"
        """

        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
