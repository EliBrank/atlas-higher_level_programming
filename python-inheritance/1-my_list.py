#!/usr/bin/python3

"""defines the function print_sorted"""


class MyList(list):
    """list holding integer values"""

    def print_sorted(self):
        """prints all integers in list in ascending order"""

        for i in self:
            if not isinstance(i, int):
                raise TypeError()

        print(sorted(self))
