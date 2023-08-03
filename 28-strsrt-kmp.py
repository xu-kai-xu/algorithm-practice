# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 07:57:24 2023

@author: xuk11
"""
haystack1 = "sadbutsad"
needle1 = "sad"

haystack2 = "leetcode"
needle2 = "leeto"

haystack3 = "aabaabaafa"
needle3 = "aabaaf"

def get_next_v1(needle):
    # 前缀表统一减一
    patn = [0] * len(needle)
    j = -1
    patn[0] = j

    for i in range(1, len(needle)):
        while (j >=0 and needle[i] != needle[j + 1]):
            j = patn[j]
        if (needle[i] == needle[j + 1]):
            j += 1
        patn[i] = j

    return patn


def get_next_v2(needle):
    # 前缀表不减一
    patn = [0] * len(needle)
    j = 0
    patn[0] = j

    for i in range(1, len(needle)):
        while (j > 0 and needle[i] != needle[j]):
            j = patn[j - 1]
        if (needle[i] == needle[j]):
            j += 1
        patn[i] = j

    return patn


def strstr_v1(s, t):
    # 在s中查找第一个与t匹配的位置
    # s 为文本串 t为模式串
    j = -1
    pattern = get_next_v1(t)
    for i in range(len(s)):
        while(j >= 0 and s[i] != t[j + 1]):
            j = pattern[j]

        if (s[i] == t[j + 1]):
            j += 1

        if (j == len(t) - 1):
            return i - len(t) + 1

    return -1


def strstr_v2(s, t):
    # 在s中查找第一个与t匹配的位置
    j = 0
    pattern = get_next_v2(t)

    for i in range(len(s)):
        while (j > 0 and s[i] != t[j]):
            j = pattern[j - 1]

        if (s[i] == t[j]):
            j += 1

        if (j == len(t)):
            return (i - len(t) + 1)

    return -1

get_next_v1(needle3)
get_next_v2(needle3)

strstr_v1(haystack3, needle3)
strstr_v2(haystack3, needle3)
