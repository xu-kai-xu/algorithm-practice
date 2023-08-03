# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:14:38 2023

@author: xuk11
454 四数相加 II
"""

# nums1 = [1, 2]
# nums2 = [-2, -1]
# nums3 = [-1, 2]
# nums4 = [0, 2]

nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]


def fourSumCount(nums1, nums2, nums3, nums4):
    hash_table = dict()
    for i in nums1:
        for j in nums2:
            if (i + j) in hash_table:
                hash_table[i + j] += 1
            else:
                hash_table[i + j] = 1

    count = 0
    for m in nums3:
        for n in nums4:
            if (0 - (m + n)) in hash_table:
                count += hash_table[0 - (m + n)]

    return count

fourSumCount(nums1, nums2, nums3, nums4)
