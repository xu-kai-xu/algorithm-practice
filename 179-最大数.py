# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:48:50 2022

@author: xuk11
"""

## 没过！

nums = [10,2]
nums = [3,30,34,5,9]

def largestNumber(nums):
    strs = list(map(str, nums))  # 转换为字符
    max_len = 1  # 找到最大长度
    for s in strs:
        max_len = max(max_len, len(s))

    # 不足最大长度的，按最后一位补足到最大长度
    num_dict = {}
    for item in strs:
        num_dict.setdefault(item, '')

    for s in strs:
        num_dict[s] = s.ljust(max_len, s[-1])

    # 排序
    seq = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)

    res = ''

    for i, j in seq:
        res += i

    return res


largestNumber(nums)