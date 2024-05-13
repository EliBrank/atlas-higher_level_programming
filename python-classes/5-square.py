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

    @property
    def size(self):
        """getter method for size

        Returns: current size of instance of Square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size

        Args:
            value: new value for size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates area of Square

        Returns: area, i.e. size, squared
        """

        return self.__size**2

    def my_print(self):
        """prints the Square to stdout"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
