# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:02:41 2023

@author: xuk11
"""

s1 = "abbaca"
s2 = "aabba"
s3 = "aaabbbccc"

with open('1047-read-string.txt', 'r') as f:
    s5 = f.read()

print(s5)


def removeDuplicates(s):
    stack = []
    for letter in s:
        if not stack:
            stack.append(letter)
            continue
        if stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)

    res = ''
    while stack:
        res += stack.pop()

    return res[::-1]


removeDuplicates(s5)
