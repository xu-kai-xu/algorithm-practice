# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:09:19 2023

@author: xuk11
计算像素矩阵的平均饱和度
"""
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix = matrix1

def saturation_sum(matrix):
    len_row = len(matrix)
    len_col = len(matrix[0])
    new_matrix = [[]] * (len_row + 2)
    new_matrix[0] = [0] * (len_col + 2)
    i = 0
    res = 0
    for i in range(len_row):
        new_matrix[i + 1] = [0] + matrix[i] + [0]

    new_matrix[-1] = [0] * (len_col + 2)
    # return new_matrix

    for i in range(len_row):
        for j in range(len_col):
            res += cal_saturation(i + 1, j + 1, new_matrix)

    return res

def cal_saturation(i, j, matrix):
    satu_sum = 0
    div = 0
    len_row = len(matrix)
    len_col = len(matrix[0])
    satu_sum = sum(matrix[i-1][j-1: j+2] + matrix[i][j-1: j+2] + matrix[i+1][j-1: j+2])
    if i == 1:
        if j == 1 or j == len_col - 2:
            div = 4
        else:
            div = 6
    elif i == len_row - 2:
        if j == 1 or j == len_col - 2:
            div = 4
        else:
            div = 6
    elif j == 1 or j == len_col - 2:
        div = 6
    else:
        div = 9

    return int(satu_sum / div)


saturation_sum(matrix1)

# new = saturation_sum(matrix1)

# for i in range(3):
#     for j in range(3):
#         print(cal_saturation(i + 1, j + 1, new))
