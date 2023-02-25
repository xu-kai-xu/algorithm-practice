# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 07:29:19 2023

@author: xuk11
https://leetcode.cn/problems/two-sum/
1 两数之和
哈希表
"""
nums1 = [2, 7, 11, 15]
targ1 = 9

nums2 = [3, 2, 4]
targ2 = 6

nums3 = [3, 3]
targ3 = 6


def twoSum(nums, target):
    hash_table = dict()
    for idx, key in enumerate(nums):
        if (target - key) in hash_table:
            return [idx, hash_table[target - key]]
        else:
            hash_table[key] = idx


twoSum(nums2, targ2)
