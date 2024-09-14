#!/usr/bin/env python3
'''defines function that transposes a matrix ,interchanging rows and columns.'''


def matrix_transpose(matrix):
   '''returns new matrix that is a transpose of the given 2D matrix'''
    result = [[None for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
  for i in range(len(matrix)):
      for j in range(len(matrix[0])):
          result[j][i] = matrix[i][j]
  return result
