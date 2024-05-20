#!/usr/bin/python3

"""defines the function write_file"""


def write_file(filename="", text=""):
    """opens, writes to file specified

    Returns: number of characters written
    """

    with open(filename, "w") as f:
        f_written = f.write(text)
        return f_written
