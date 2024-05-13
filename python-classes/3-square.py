#!/usr/bin/python3

"""establishes class Square"""


class Square:
    """Square is instatiated with size"""
    def __init__(self, size=0):
        """defines size with instance

        Args:
            size (opt): side length of Square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates area of Square

        Returns: area - size, squared
        """

        return self.__size**2
