# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 07:47:32 2023

@author: xuk11

344 翻转字符串
"""

s1 = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]
s3 = ['a']
s4 = []

def reverseString(s):
    size = len(s)
    i = 0
    j = size - 1
    while i < j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        i += 1
        j -= 1

reverseString(s1)
reverseString(s2)
reverseString(s3)
reverseString(s4)
