# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 07:51:18 2023

@author: xuk11
459-repeated sub string
https://leetcode.cn/problems/repeated-substring-pattern/
"""

s1 = "abab"
s2 = "aba"
s3 = "abcabcabcabc"
s4 = "abcfabcfabcf"
s5 = "aabaaf"


def longest_common_substr(s):
    match = [0] * len(s)
    j = -1
    match[0] = -1
    for i in range(1, len(s)):
        while (j >= 0 and s[j + 1] != s[i]):
            j = match[j]

        if (s[j + 1] == s[i]):
            j += 1

        match[i] = j

    return match


def repeated_sub_str_v1(s):
    comp = (s + s)[1: -1]
    if s in comp:
        return True
    return False


def repeated_sub_str_v2(s):
    match_res = longest_common_substr(s)
    if match_res[-1] == -1:
        return False
    if (len(s) % (len(s) - match_res[-1] - 1) != 0):
        return False
    return True

repeated_sub_str_v1(s1)
repeated_sub_str_v2(s1)
