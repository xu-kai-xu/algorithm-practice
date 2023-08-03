# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:22:30 2023

@author: xukkk
39 组合总和
https://leetcode.cn/problems/combination-sum/
"""

candidates = [2,3,6,7]
target = 7

# candidates = [2,3,5]
# target = 8

# candidates = [2]
# target = 1


def backtracking(candidates, target, path, res, idx):
    if sum(path) == target:
        res.append(path.copy())
        return
    
    if sum(path) > target:
        return
    
    for i in range(idx, len(candidates)):
        path.append(candidates[i])
        backtracking(candidates, target, path, res, i)
        path.pop()
    

def combinationSum(candiates, target):
    path = []
    res = []
    idx = 0
    
    backtracking(candidates, target, path, res, idx)
    
    return res


combinationSum(candidates, target)
    

