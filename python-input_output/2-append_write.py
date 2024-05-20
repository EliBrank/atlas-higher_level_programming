#!/usr/bin/python3

"""defines the function append_write"""


def append_write(filename="", text=""):
    """appends string to the end of specified text file

    Returns: number of characters added
    """

    with open(filename, "a") as f:
        f_appended = f.write(text)
        return f_appended
