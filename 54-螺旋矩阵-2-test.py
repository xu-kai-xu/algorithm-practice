# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:44:37 2022

@author: xuk11
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

mask = []
for i in range(len(matrix)):
    mask.append([])
    for j in range(len(matrix[0])):
        mask[i].append(True)  # 记录矩阵的遍历情况