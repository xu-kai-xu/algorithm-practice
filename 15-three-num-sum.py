# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:51:52 2023

@author: xuk11
15 三数之和
"""

nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]

nums = nums1

def threeSum(nums, target):
    res = []
    nums = sorted(nums)
    size = len(nums)
    i = 0
    while i < size:
        left = i + 1
        right = size - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums < target:
                left += 1
            elif sums > target:
                right -= 1
            elif sums == target:
                tmp = (nums[i], nums[left], nums[right])
                if tmp not in res:
                    res.append(tmp)
                left += 1
        i += 1
    res = [list(tup) for tup in res]
    return res

threeSum(nums1)
