# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:25:57 2022

@author: xuk11
"""

s = 'A Famous Saying: Much Ado About Nothing (2012/8).'
a = ''
for i in s:
    if i.isalpha():
        a += i

b = sorted(a, key=str.upper)

index = 0
d = ''
for i in range(len(s)):
    if s[i].isalpha():
        d += b[index]
        index += 1
    else:
        d += s[i]
print(d)
