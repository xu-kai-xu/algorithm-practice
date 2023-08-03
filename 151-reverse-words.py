# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 07:20:47 2023

@author: xuk11
"""
s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"

def reverseWords(s):
    tmp = s[::-1].split(' ')
    res = []
    for word in tmp:
        if word:
            res.append(word[::-1])
    return ' '.join(res)

reverseWords(s3)
