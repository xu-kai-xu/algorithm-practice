# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:34:20 2022

@author: xuk11
"""


nums = [20,70,110,150]
target = 90

def twoSum(nums, target):
    res = []
    hash = dict()
    for i in range(len(nums)):
        tmp = target - nums[i]
        if tmp not in hash:
            hash[nums[i]] = i
        else:
            res.append(hash[tmp] + 1)
            res.append(i + 1)
    return res