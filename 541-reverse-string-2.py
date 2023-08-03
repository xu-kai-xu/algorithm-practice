# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 07:31:05 2023

@author: xuk11
541 翻转字符串-2
"""

s1 = 'abcdefg'
k1 = 2

s2 = 'abcd'
k2 = 2

def findRev(s, k):
    size = len(s)
    sRev = ''
    sKep = ''
    if size < k:
        sRev += s
        s = s[size:]
    elif size >= k and size < 2 * k:
        sRev += s[:k]
        sKep += s[k: size]
        s = s[size:]
    else:
        sRev += s[:k]
        sKep += s[k: 2 * k]
        s = s[2 * k:]
    return [s, sRev, sKep]

def reverseStr(s, k):
    sRev = ''
    sKep = ''
    res = ''
    while s:
        s, sRev, sKep = findRev(s, k)
        res += sRev[::-1]
        res += sKep

    return res

reverseStr('', k2)
