# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:40:22 2023

@author: xukkk

40-组合总和2
https://leetcode.cn/problems/combination-sum-ii/
"""

# candidates = [10,1,2,7,6,1,5]
# target = 8

# candidates = [2,5,2,1,2]
# target = 5

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27


def backtracking(candidates, target, path, res, idx):
    # used 数组去重
    # if sum(path) == target and path not in res:
    if sum(path) == target:
        res.append(path.copy())
        return
    if sum(path) > target:
        return
    
    for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i - 1]:
            continue
        path.append(candidates[i])
        backtracking(candidates, target, path, res, i+1)
        path.pop()


def combinationSum2(candidates, target):
    candidates.sort()
    res = []
    path = []
    idx = 0
    used = [0] * len(candidates)
    
    backtracking(candidates, target, path, res, idx)
       
    return res


combinationSum2(candidates, target)


