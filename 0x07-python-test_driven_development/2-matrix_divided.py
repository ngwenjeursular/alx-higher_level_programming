#!/usr/bin/python3
"""
This module defines a function for dividing elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    :param matrix: list of lists of int or float, the input matrix
    :param div: int or float, the divisor

    :return: list of lists of float, a new matrix with elements divided by div
    (rounded to two decimal places)

    :raises:
        - TypeError: if matrix isn't a list of lists of int
        - or float or if each row has a different size
        - TypeError: if div is not a number (int or float)
        - ZeroDivisionError: if div is equal to 0
    """
    matr_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not all(
            isinstance(row, list)
            and all(isinstance(val, (int, float)) for val in row)
            for row in matrix
    ):
        raise TypeError(matr_error)

    # Checking if each row has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (int or float) and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix elements by div and round to 2 decimal places
    result = [[round(val / div, 2) for val in row] for row in matrix]

    return result
