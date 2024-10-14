#!/usr/bin/env python3
'''
corelation function
'''
import numpy as np


def correlation(C):
    """
    Function that calculates a correlation matrix
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2:
        raise TypeError("C must be a 2D numpy.ndarray")
    if C.shape[0] < 2:
        raise ValueError("C must be a 2D square matrix")
    diag = np.diag(C) ** 0.5
    outer = np.outer(diag, diag)
    corr = C / outer
    return corr
