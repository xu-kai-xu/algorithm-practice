# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:17:34 2022

@author: xuk11

这题读不懂
"""

#raw = '3 abc bca cab abc 1'
raw = ''
tmp = raw.split(' ')
n = tmp[0]
k = tmp[-1]
x = tmp[-2]

tmp.remove(tmp[0])
tmp.remove(k)
tmp.remove(x)

n = int(n)
k = int(k)

num = []
for item in tmp:
    if (sorted(item) == sorted(x)) and (item != x):
        num.append(item)

print(len(num))
num.sort()
try:
    print(num[k-1])
except IndexError:
    pass


