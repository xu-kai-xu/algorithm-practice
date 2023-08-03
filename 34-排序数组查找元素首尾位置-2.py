# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:11:22 2022

@author: xuk11

https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

34 排序数组中查找元素的第一个和最后一个位置
找出来的左右边界是不包括target的边界
"""

nums = [1]
target = 1

def leftBound(nums, target):
    """寻找target的左边界，不包括target"""
    left = 0
    right = len(nums) - 1
    leftBound = -2  # 记录一下 leftBound 没有被赋值，即在区间外的情况
    while left <= right:
        mid = left + int((right - left) / 2)
        if nums[mid] >= target:
            right = mid - 1
            leftBound = right
        else:
            left = mid + 1

    return leftBound


def rightBound(nums, target):
    """寻找target的右边界"""
    left = 0
    right = len(nums) - 1
    rightBound = -2
    while left <= right:
        mid = left + int((right - left) / 2)
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            rightBound = left

    return rightBound


def searchRange(nums, target):
    leftbound = leftBound(nums, target)
    rightbound = rightBound(nums, target)

    if (leftbound == -2) or (rightbound == -2):
        return [-1,-1]
    elif rightbound - leftbound > 1:
        return [leftbound + 1,rightbound - 1]
    else:
        return [-1,-1]


t = searchRange(nums, target)

