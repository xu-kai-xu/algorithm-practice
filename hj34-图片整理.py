# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:47:06 2022

@author: xuk11
"""

raw = 'Ihave1nose2hands10fingers'

pic = {}

for s in raw:
    pic[ord(s)] = s

nums = [ord(s) for s in raw]

num_seq = sorted(nums)

res = [pic[num] for num in num_seq]

print(''.join(res))