#!/usr/bin/python3

"""defines the class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """base for Rectangle, Square classes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

    @property
    def x(self):
        """getter method for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x

        Args:
            x: horizontal offset
        """

        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter method for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y

        Args:
            y: vertical offset
        """

        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
