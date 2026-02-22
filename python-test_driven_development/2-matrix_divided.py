#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It validates the matrix structure, element types, and the divisor
before performing division rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    Raises TypeError or ZeroDivisionError for invalid inputs.
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    size_error = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(matrix_error)

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(matrix_error)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(size_error)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
