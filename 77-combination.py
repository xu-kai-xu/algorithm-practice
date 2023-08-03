# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:11:32 2023

@author: xukkk
77 组合
https://leetcode.cn/problems/combinations/
"""

import copy

n = 4
k = 2

# n = 1
# k = 1

def backtracking(n, k, startIdx, path, res):
    if len(path) == k:
        tmp = path.copy()
        res.append(tmp)
        return

    for i in range(startIdx, n - (k - len(path)) + 2):
        path.append(i)
        backtracking(n, k, i + 1, path, res)
        path.pop()


def combine(n, k):
    startIdx = 1
    path = []
    res = []
    
    backtracking(n, k, startIdx, path, res)
    
    return res


combine(n, k)
