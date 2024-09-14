#!/usr/bin/env python3
def matrix_shape(matrix):
'''defines function that calculates the shape of a matrix'''


def matrix_shape(matrix):
    '''returns list of ints of the dimensions of given matrix'''
    findshape = []
    while type(matrix) == list:
        findshape.append(len(matrix))
        matrix = matrix[0]
    return findshape
