#!/usr/bin/env python3
"""one hot encode"""
import numpy as np


def one_hot_encode(Y, classes):
    """
    One hot encode
    """
    if not isinstance(Y, np.ndarray) or len(Y.shape) == 1:
        return None
    if not isinstance(classes, int) or classes <= np.amax(Y):
        return None

    m = Y.shape[0]
    one_hot = np.zeros((classes, m))

    for idx, val in enumerate(Y):
        if val >= classes or val < 0:
            return None
        one_hot[val][idx] = 1

    return one_hot
