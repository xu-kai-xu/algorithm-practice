# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 07:36:10 2023

@author: xuk11

349-set intersection
"""
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]
nums5 = [4,7,9,7,6,7]
nums6 = [5,0,0,6,1,6,2,2,4]

def intersection(nums1, nums2):
    intersect_one = dict()
    intersect_two = dict()
    for item in nums1:
        intersect_one.setdefault(item, 1)
    print(intersect_one)
    for item in nums2:
        intersect_two.setdefault(item, 1)
    print(intersect_two)
    res = [key for key in intersect_one.keys() if intersect_two.get(key)]

    return res

def intersection(nums1, nums2):
    res = []
    intersect = dict()
    for item in nums1:
        intersect[item] = 1
    # print(intersect)
    for item in nums2:
        if item in intersect.keys() and intersect[item] == 1:
            res.append(item)
            intersect[item] = 0
    # print(intersect)

    return res

intersection(nums5, nums6)
