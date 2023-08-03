# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:54:34 2023

@author: xukkk

93- 复原ip地址
"""

s1 = "25525511135"
s2 = "0000"
s3 = "101023"
s4 = "1111"
s5 = "010010"
s6 = "101023"


def isIPNum(s):
    # 判断分割出的单个字符串是否符合ip地址的要求
    if s == '':
        return False
    if len(s) >1 and s[0] == '0':
        return False
    if int(s) > 255:
        return False
    
    return True


def backtracking(s, idx, path, res):
    if len(path) == 4 and len(''.join(path)) == len(s):
        # 长度为4 且用完了所有字符
        res.append('.'.join(path))
        return
    
    if len(path) > 4:
        return
    
    for i in range(idx, len(s) + 1):
        cut = s[idx: i]
        if isIPNum(cut):
            path.append(cut)
            backtracking(s, i, path, res)
            path.pop()
        else:
            continue
    

def restoreIpAddresses(s):
    res = []
    path = []
    idx = 0
    
    backtracking(s, idx, path, res)
    
    return res
    

restoreIpAddresses(s6)