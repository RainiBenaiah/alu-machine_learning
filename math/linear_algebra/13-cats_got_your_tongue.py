#!/usr/bin/env python3

""" defines function that concatenates two matrices along a specific  axis using numpy """

import numpy as np


def np_cat(mat1, mat2, axis=0):
    '''
    returns concatenation of  two matrices along a specific axis
    '''
    return np.concatenate((mat1, mat2), axis=axis))
