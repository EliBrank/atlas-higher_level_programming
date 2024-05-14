#!/usr/bin/python3

"""establishes the class Rectangle"""


class Rectangle:
    """Rectangle shape defined by width and height"""

    def __init__(self, width=0, height=0):
        """instanstiation of Rectangle class

        Args:
            width (opt): horizontal side length
            height (opt): vertical side length
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """getter method for width

        Returns: current width of Rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width

        Args:
            value: new value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method for height

        Returns: current height of Rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height

        Args:
            value: new value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates area of Rectangle

        Returns: area, i.e. width multiplied by height
        """

        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of Rectangle

        Returns: perimeter, i.e. sum of lengths of each side
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """re-formats print output of Rectangle pictorally

        Returns: Rectangle represented using "#" characters
        """

        print_result = ""
        if self.__width != 0 and self.__height != 0:
            for row in range(self.__height):
                for i in range(self.__width):
                    print_result += '#'
                # does not print newline on last row
                if row != self.__height - 1:
                    print_result += '\n'

        return print_result

    def __repr__(self):
        """formats repr output to print instanstiation instructions

        Returns: call to Rectangle class with same parameters as self
        """

        return f"Rectangle({self.__width}, {self.__height})"
