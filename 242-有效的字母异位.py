# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 07:27:02 2023

@author: xuk11
"""


def isAnagram(s, t):
    word = dict()
    for i in range(26):  # 初始化字典
        word.setdefault(chr(97 + i), 0)
    for letter in s:  # 标记s中的字母
        word[letter] += 1
    for letter in t:  # 标记t中的字母
        word[letter] -= 1
    word_set = set(word.values())
    if len(word_set) == 1 and (0 in word_set):
        return True
    return False
