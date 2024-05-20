#!/usr/bin/python3

"""defines the class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines Square based on Rectangle"""
    def __init__(self, size): 

        """instantiates with size

        Args:
            size: side length
        """

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
