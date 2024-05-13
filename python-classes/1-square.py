#!/usr/bin/python3

"""establishes class Square"""


class Square:
    """Square is instatiated with size"""
    def __init__(self, size):
        """defines size with instance

        Args:
            size: side length of Square
        """

        self.__size = size
