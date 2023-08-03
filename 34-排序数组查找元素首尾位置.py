# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

34 排序数组中查找元素的第一个和最后一个位置
"""

nums = [5,7,7,8,8,8,8,8,8,10]
target = 8

def binSearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + int((right - left) / 2)
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            return mid

    return -1  # not found

def searchRange(nums, target):
    pass
    ser = binSearch(nums, target)
    if ser == -1:
        return -1
    elif ser != -1:
        return [ser, binSearch(nums[:ser], target), binSearch(nums[ser+1:], target) + ser + 1]

binSearch(nums, target)
t = searchRange(nums, target)
res = [i for i in t if i != -1]
res.sort()
