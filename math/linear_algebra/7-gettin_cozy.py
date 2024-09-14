#!/usr/bin/env python3
""" defines function that concatenates two 2D matrices along an axis """


def cat_matrices2D(mat1, mat2, axis=0):
     '''
    Concatenates two 2D matrices along a specific axis
    '''
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    newmat = []
    for i in range(len(mat1)):
        newmat.append(mat1[i][:])
    if axis == 0:
        for i in range(len(mat2)):
            newmat.append(mat2[i][:])
    elif axis == 1:
        for i in range(len(mat1)):
            newmat[i] += mat2[i]
    return newmat
