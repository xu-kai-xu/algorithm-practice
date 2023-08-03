# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:01:23 2023

@author: xukkk
46 全排列
"""

nums = [0, 1]
nums = [1]
nums = [1, 2, 3]


def backtracking(nums, path, res, used):
    if len(path) == len(nums):
        res.append(path.copy())
        return
    
    for i in range(len(nums)):
        if used[i]:
            continue
        path.append(nums[i])
        used[i] = 1
        backtracking(nums, path, res, used)
        path.pop()
        used[i] = 0
        
# 如果不要used，       
# def backtracking(nums, path, res):
#     if len(path) == len(nums):
#         res.append(path.copy())
#         return
    
#     for i in range(len(nums)):
#         path.append(nums[i])
#         backtracking(nums, path, res)
#         path.pop()


def permute(nums):
    path = []
    res = []
    used = [0] * len(nums)

    backtracking(nums, path, res, used)
    
    return res


permute([1, 0])