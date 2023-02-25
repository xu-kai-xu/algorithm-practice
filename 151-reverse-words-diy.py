# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 07:20:47 2023

@author: xuk11
"""
s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"

def reverseWords(s):
    tmp = s[::-1]
    res = []
    size = len(tmp)
    i = j = 0
    while j < size:
        if (tmp[i] == ' '):
            i += 1
            j = i
            continue
        if (tmp[j] != ' '):
            j += 1
            continue
        res.append(tmp[i: j][::-1])
        i = j

    if tmp[j-1] != ' ':
        res.append(tmp[i:][::-1])

    return ' '.join(res)

reverseWords(s3)
