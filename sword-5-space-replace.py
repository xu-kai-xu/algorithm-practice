# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 07:36:47 2023

@author: xuk11
剑指offer5 替换空格
"""
s = 'We are happy.'

def replaceSpace(s):
    res = []
    for letter in s:
        if letter == ' ':
            res.append('%20')
        else:
            res.append(letter)

    return ''.join(res)

replaceSpace(s)
