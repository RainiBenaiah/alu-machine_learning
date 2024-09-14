#!/usr/bin/env python3
"""Defines a function that multiplies two matrices."""

import numpy as np

def mat_mul(mat1, mat2):
    """Returns a new matrix that is the product of two 2D matrices."""

    if len(mat1[0]) != len(mat2):
        return None

    return np.dot(mat1, mat2)
