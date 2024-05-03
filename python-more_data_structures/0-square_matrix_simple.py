#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # List comprehension
    # Inner list square each value for a row
    # Outer list composed of each completed row
    return [[x * x for x in row] for row in matrix]
