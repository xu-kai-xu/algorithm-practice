# -*- coding: utf-8 -*-
"""
Created on Sat Nov 5 17:39:57 2022

@author: xuk11
"""
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

def spiralOrder(matrix):
    res = []  # 记录最终结果
    tmp = matrix
    size = len(matrix) * len(matrix[0])

    while len(tmp) != 0:

        # 上层 从左向右
        res.extend(tmp[0])
        tmp = tmp[1:]

        if len(res) == size:
            break

        # 右列 从上到下
        for row in tmp:
            res.append(row[-1])
        for i in range(len(tmp)):
            tmp[i] = tmp[i][:-1]

        if len(res) == size:
            break

        # 下列 从右向左
        res.extend(tmp[-1][::-1])
        tmp = tmp[:-1]

        if len(res) == size:
            break

        # 左列 从下到上
        for row in tmp[::-1]:
            res.append(row[0])
        for i in range(len(tmp)):
            tmp[i] = tmp[i][1:]

        if len(res) == size:
            break

    return res


spiralOrder(matrix)
