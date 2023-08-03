# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 07:28:20 2023

@author: xuk11
1047 删除字符串中所有相邻重复项
"""

s1 = "abbaca"
s2 = "aabba"
s3 = "aaabbbccc"

with open('1047-read-string.txt', 'r') as f:
    s5 = f.read()

print(s5)


def removeDuplicates(s):
    letters = list(s)
    stack = []

    while letters:
        if not stack:
            stack.append(letters.pop(0))

        if letters:
            tmp = letters.pop(0)
        else:
            break
        if tmp == stack[-1]:
            stack.pop()
        else:
            stack.append(tmp)

    res = ''
    while stack:
        res += stack.pop()

    return res[::-1]


removeDuplicates(s3)
removeDuplicates("a")
