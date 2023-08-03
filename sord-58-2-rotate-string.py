# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 07:51:36 2023

@author: xuk11
"""

s1 = "abcdefg"
k1 = 2

s2 = "lrloseumgh"
k2 = 6

s3 = "t"
k3 = 1

s = s1
k = k1


def reversewords(s):
    i = 0
    size = len(s)
    j = size - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


def reverseLeftWords(s, n):
    word_lst = list(s)
    word_lst[: n] = reversewords(word_lst[: n])
    word_lst[n:] = reversewords(word_lst[n:])
    word_lst = reversewords(word_lst)
    return ''.join(word_lst)


reverseLeftWords(s3, k3)
