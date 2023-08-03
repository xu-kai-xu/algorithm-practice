# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 07:39:54 2023

@author: xuk11
27 移除元素
"""

nums1 = [3, 2, 2, 3]
val1 = 3

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2


def remove_elements(nums, val):
    i = j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j


remove_elements(nums1, val1)
# remove_elements(nums2, val2)
