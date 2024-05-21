#!/usr/bin/python3

"""defines function pascal_triangle"""


def pascal_triangle(n):
    """creates pascal triangle

    Returns: list of lists - each list contains row of triangle
    """

    triangle_matrix = []

    if n <= 0:
        return triangle_matrix

    for i in range(n):
        row = []
        triangle_matrix.append(row)
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle_matrix[i - 1][j] +
                triangle_matrix[i - 1][j - 1])

    return triangle_matrix
