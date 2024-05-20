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

        super().__init__(size, size)

    def area(self):
        """calculates Square area based on size

        Returns: area, i.e. width multiplied by height
        """
        return self._Rectangle__width * self._Rectangle__height
