#!/usr/bin/python3

"""defines function pascal_triangle"""


def pascal_triangle(n):
    """creates pascal triangle

    Returns: list of lists - each list contains row of triangle
    """

    matrix = []

    if n <= 0:
        return matrix

    for i in range(n):
        row = []
        matrix.append(row)
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(matrix[i - 1][j] + matrix[i - 1][j - 1])

    return matrix
