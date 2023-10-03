#!/usr/bin/python3
"""Define a matrix division."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor

    Args:
    matrix: The list of lists containing integers or floats.
    div: The number (integer or float) by which matrix elements are divided.

    Returns:
    A new matrix with the divided elements, rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers/floats,
               if rows have different sizes, or if div is not a number.
    ZeroDivisionError: If div is zero.
    """

    # Check matrix type and content validity
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check uniformity in row sizes
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check divisor type and value
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide and round matrix elements
    return [[round(num / div, 2) for num in row] for row in matrix]
