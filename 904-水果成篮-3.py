# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:01:09 2022

@author: xuk11
"""
from collections import Counter

def totalFruit(fruits):
    cnt = Counter()
    j = 0
    res = 0
    for i, x in enumerate(fruits):
        cnt[x] += 1
        while len(cnt) > 2:
            y = fruits[j]
            cnt[y] -= 1
            if cnt[y] == 0:
                cnt.pop(y)
            j += 1
        #res = max(res, i - j + 1)
        length = i - j + 1
        if res < length:
            res = length

    return res

fruits = [3,3,3,1,2,1,1,2,3,3,4]
#fruits = [1, 2, 1]
#fruits = [0,1,2,2]
t = totalFruit(fruits)
print(t)