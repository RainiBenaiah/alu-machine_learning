#!/usr/bin/env python3
# Transposing a matrix means interchanging rowa and columns.
# for i in range(len(matrix));
#   for j in range(len(matrix[0]));
#   result[j][i = matrix[i][j]]
# for y in result:
#  print(y)
# simplified example below:
def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))
