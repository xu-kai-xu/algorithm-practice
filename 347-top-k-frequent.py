# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 06:59:55 2023

@author: xuk11
# 347 前k个高频元素
"""
nums1 = [1,1,1,2,2,3]
k1 = 2

nums2 = [1]
k2 = 1

def topKFrequent(nums, k):
    freq_dict = {}
    for num in nums:
        if freq_dict.get(num):
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    new_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    res = []
    for i in range(k):
        res.append(new_dict[i][0])

    return res


topKFrequent(nums2, k2)
