# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 08:49:43 2023

@author: xukkk
216 组合总和
"""

import copy

# k = 3
# n = 7

# k = 3
# n = 9

k = 4
n = 1


def backtracking(k, n, startIdx, path, res):
    if len(path) == k and sum(path) == n:
        tmp = path.copy()
        res.append(tmp)
        return
    if sum(path) > n:
        return
    
    for i in range(startIdx, 10):
        path.append(i)
        backtracking(k, n, i + 1, path, res)
        path.pop()


def combinationSum3(k, n):
    path = []
    res = []
    startIdx = 1
    
    backtracking(k, n, startIdx, path, res)
    
    return res


combinationSum3(k, n)