#!/usr/bin/python3

"""defines the class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """a square shape which can be modified and printed"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiates Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """re-formats Square printout to display class and properties

        Returns: [<class>] (<id>) <x>/<y> - <width>/<height>
        """

        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")
