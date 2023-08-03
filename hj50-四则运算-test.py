# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:50:04 2022

@author: xuk11
"""
import re

raw = '3+2*{1+2*[-4/(8-6)+7]}'
#raw = '3*5+8-0*3-6+0+0'
#raw = '5-3+9*6*(6-10-2)'
raw = raw.replace('{', '(')
raw = raw.replace('}', ')')
raw = raw.replace('[', '(')
raw = raw.replace(']', ')')

raw = re.sub(r'[(](-\d)', r'((0\1)', raw)


# 初步切割
def first_cut(strs):
    """切割输入字符串，返回数和运算符的列表"""
    res = []
    num = ''
    opes = ['+', '-', '*', '/', '(', ')']
    for s in strs:
        if s not in opes:
            num += s
        else:
            res.append(num)
            res.append(s)
            num = ''

    if len(num) != 0:
        res.append(num)

    for item in res:
        if len(item) == 0:
            res.remove(item)

    return res



t = first_cut(raw)

print(t)

