# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:24:57 2023

@author: xukkk
131-切割回文串
https://leetcode.cn/problems/palindrome-partitioning/
要求每个子串都是回文串，所以如果出现一个不是回文串，就可以结束了
"""
s = 'aab'
# s = 'a'

def is_palindrome(s):
    if s == '':
        return False
    if len(s) == 1:
        return True
    
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
        

def backtracking(s, idx, path, res):
    if idx >= len(s):
        res.append(path.copy())
        return
    
    for i in range(idx, len(s) + 1):
        cut = s[idx: i]
        if is_palindrome(cut):
            path.append(cut)
        else:
            continue
        backtracking(s, i, path, res)
        path.pop()
        

def partition(s):
    path = []
    res = []
    idx = 0
    
    backtracking(s, idx, path, res)
    
    return res

    
partition(s)
