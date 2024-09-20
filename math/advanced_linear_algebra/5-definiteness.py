#!/usr/bin/env python3
"""
defines a function that Calculates the definiteness of a matrix.
"""


import numpy as np


def definiteness(matrix):
  """
    matrix: A numpy.ndarray of shape (n, n) whose definiteness should be calculated.

  Returns:
    The string "Positive definite",
    "Positive semi-definite", "Negative semi-definite", "Negative definite", or "Indefinite"
    if the matrix is positive definite, positive semi-definite,
    negative semi-definite, negative definite of indefinite, respectively.
    If matrix does not fit any of the above categories, return None.

  Raises:
    TypeError: If matrix is not a numpy.ndarray.
  """

  if not isinstance(matrix, np.ndarray):
    raise TypeError("matrix must be a numpy.ndarray")
  
  if len(matrix.shape) < 2:
    return None

  if matrix.shape[0] != matrix.shape[1]:
    return None  # Not a square matrix

  eigenvalues = np.linalg.eigvals(matrix)

  if all(eigenvalues > 0):
    return "Positive definite"
  elif all(eigenvalues >= 0):
    return "Positive semi-definite"
  elif all(eigenvalues < 0):
    return "Negative definite"
  elif all(eigenvalues <= 0):
    return "Negative semi-definite"
  else:
    return "Indefinite"
  
