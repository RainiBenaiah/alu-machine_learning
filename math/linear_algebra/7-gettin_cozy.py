#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
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

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
print(mat4)
print(mat5)
mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)
print(mat4)
print(mat5)
