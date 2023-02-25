# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 07:39:30 2023

@author: xuk11
"""
nums1 = [1, 0, -1, 0, -2, 2]
targ1 = 0

nums2 = [2, 2, 2, 2, 2]
targ2 = 8

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


def fourSum(nums, target):
    res = []
    nums = sorted(nums)
    size = len(nums)
    for i in range(size):
        three = [nums[j] for j in range(size) if j != i]
        res_three = threeSum(three, target - nums[i])
        for lst in res_three:
            lst.insert(0, nums[i])
            lst.sort()
            if lst not in res:
                res.append(lst)
    return res

fourSum(nums1, targ1)
