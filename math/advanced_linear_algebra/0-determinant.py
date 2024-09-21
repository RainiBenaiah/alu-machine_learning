#!/usr/bin/env python3

"""
Defines a function that Calculates the determinant of a square matrix.
"""

def determinant(matrix):
    """
    matrix: A list of lists representing a square matrix.

    Returns:
        The determinant of the matrix.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0:
        raise ValueError("matrix must be a square matrix")

    # Handle the case of an empty matrix (0x0)
    if matrix == [[]]:
        return 1

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(n):
        submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]

        sign = (-1)**i
        det += sign * matrix[0][i] * determinant(submatrix)

    return det
