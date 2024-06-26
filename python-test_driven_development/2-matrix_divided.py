#!/usr/bin/python3

"""defines function matrix_divided"""


def matrix_divided(matrix, div):
    """divides each entry of matrix by a value

    Args:
        matrix: list of lists of values to be divided
        div: divisor for matrix values

    Returns: new matrix with divided values
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    

    for row in matrix:
        if 
        for a in row:
            if isinstance(a, float):
                a = int(a)
            if not isinstance(a, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            
