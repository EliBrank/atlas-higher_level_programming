#!/usr/bin/python3

"""defines the class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """a rectangle shape which can be modified and printed"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

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

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

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

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

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

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """calculates area of Rectangle

        Returns: area, i.e. width multiplied by height
        """

        return self.width * self.height

    def display(self):
        """prints Rectangle pictorally using '#'"""

        print_result = ""
        for row_offset in range(self.y):
            print_result += '\n'
        for row in range(self.height):
            for column_offset in range(self.x):
                print_result += " "
            for column in range(self.width):
                print_result += str("#")
            # does not print newline on last row
            if row != self.height - 1:
                print_result += '\n'

        print(print_result)

    def update(self, *args, **kwargs):
        """reassigns attributes based on input

        Args:
            args: (id, width, height, x, y) in order
            kwargs: any number of attr=attr_value pairs
        """

        attr_order = ["id", "width", "height", "x", "y"]

        if args is not None and len(args) > 0:
            for index, arg in enumerate(args):
                setattr(self, attr_order[index], arg)
        else:
            for attr, attr_value in kwargs.items():
                setattr(self, attr, attr_value)

    def __str__(self) -> str:
        """re-formats Rectangle printout to display class and properties

        Returns: [<class>] (<id>) <x>/<y> - <width>/<height>
        """

        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")
