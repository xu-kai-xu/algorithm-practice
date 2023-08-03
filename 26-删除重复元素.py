# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:03:13 2022

@author: xuk11
"""

nums = [1,1,2]

def removeDuplicates(nums):
    slow = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[slow]:
            slow += 1
            nums[slow] = nums[i]

    return slow

t = removeDuplicates(nums)
nums[:t+1]
