# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 09:19:09 2022

@author: xuk11
"""
import re

raw = ['abcd12345ed125ss123058789', 'a8a72a6a5yy98y65ee1r2']

for string in raw:
    nums = re.findall(r'\d+', string)
    size = [len(item) for item in nums]
    max_size = max(size)
    mask = [item >= max_size for item in size]
    res = ''
    for i in range(len(size)):
        if mask[i] == True:
            res += nums[i]

    print(res + ',' + str(max_size))
