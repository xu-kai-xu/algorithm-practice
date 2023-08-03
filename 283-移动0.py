# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:10:05 2022

@author: xuk11

https://leetcode.cn/problems/move-zeroes/

"""

nums1 = [0,1,0,3,12]
nums2 = [1]

nums = nums1

def moveZeros(nums):
    slow, fast = 0, 0
    size = len(nums)

    while fast < size:
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1

moveZeros(nums)
print(nums)




