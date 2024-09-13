#!/usr/bin/env python3

def add_matrices2D(mat1, mat2):
   if len(mat1) != len(mat2):
      if len(mat1[0]) != len(mat2[0]):
         return None
   sum_matrix = [[0 for i in range(len(mat1[0]))] for j in range(len(mat1))]
   for i in range(len(mat1)):
        for j in range (len(mat1[0])):
            sum_matrix[i][j] = (mat1[i][j] + mat2[i][j])
   return sum_matrix
   """ if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
"""
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
