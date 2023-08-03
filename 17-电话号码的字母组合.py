# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:07:20 2023

@author: xukkk
17 电话号码的字母组合
https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
"""

digits = '23'
digits = '234'
# digits = ''
# digits = '2'


def backtracking(digits, phoneMap, idx, path, res):
    if idx == len(digits):
        res.append(path)
        return
    
    num = digits[idx]
    letters = phoneMap[num]
    for i in range(len(letters)):
        path += letters[i]
        backtracking(digits, phoneMap, idx+1, path, res)
        path = path[:-1] 


def letterCombinations(digits):
    phoneMap = {'1': None,
                '2': ('a', 'b', 'c'),
                '3': ('d', 'e', 'f'),
                '4': ('g', 'h', 'i'),
                '5': ('j', 'k', 'l'),
                '6': ('m', 'n', 'o'),
                '7': ('p', 'q', 'r', 's'),
                '8': ('t', 'u', 'v'),
                '9': ('w', 'x', 'y', 'z')}
    
    idx = 0
    path = ''
    res = []
    
    backtracking(digits, phoneMap, idx, path, res)
    
    return res


letterCombinations('2')
    
    
    

