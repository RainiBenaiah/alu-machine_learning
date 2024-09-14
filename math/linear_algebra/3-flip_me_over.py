#!/usr/bin/env python3
'''defines function that transposes a matrix ,interchanging rows and columns.'''


def matrix_transpose(matrix):
   '''returns new matrix that is a transpose of the given 2D matrix'''
     return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
