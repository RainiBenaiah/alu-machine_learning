#!/usr/bin/env python3
""" defines function that slices a matrix using numpy  along specific axes """



def np_slice(matrix, axes={}):
    """
    returns a num.array, slices a matrix along specific axes.
    """
    return matrix[axes.get(0, slice(None)), axes.get(1, slice(None))]
