#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix by.

    Returns:
        list of lists: The new matrix with elements divid by 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number (integer or float).
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix list of int/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix lists) of int/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
