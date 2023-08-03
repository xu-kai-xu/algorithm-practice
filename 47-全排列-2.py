# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:01:23 2023

@author: xukkk
47 全排列-2
"""

nums = [1, 1, 2]
nums = [1, 2, 3]


def backtracking(nums, path, res, used):
    if len(path) == len(nums):
        res.append(path.copy())
        return
    
    for i in range(len(nums)):
        if (i > 0) and (nums[i] == nums[i - 1]) and (used[i - 1] == 0):
            continue
        if used[i]:
            continue
        path.append(nums[i])
        used[i] = 1
        backtracking(nums, path, res, used)
        path.pop()
        used[i] = 0


def permuteUnique(nums):
    nums.sort()
    path = []
    res = []
    used = [0] * len(nums)

    backtracking(nums, path, res, used)
    
    return res


permuteUnique(nums)