#!/usr/bin/python3

"""establishes class Square"""


class Square:
    """Square is instatiated with size"""
    def __init__(self, size=0, position=(0,0)):
        """instantiates Square

        Args:
            size (opt): side length of Square
            position (opt): grid offset for Square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if len(position) != 2 or not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """getter method for position

        Returns: current position of instance of Square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """setter method for position

        Args:
            value: new value for position
        """

        if len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value


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
                for j in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
