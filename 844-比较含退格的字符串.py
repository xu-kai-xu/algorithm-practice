# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:52:34 2022

@author: xuk11
https://leetcode.cn/problems/backspace-string-compare/
"""

# s = "ab#c"
# t = "ad#c"

# s = "ab##"
# t = "c#d#"

# s = "a##c"
# t = "#a#c"

s = "y#fo##f"
t = "y#f#o##f"

def string_process(strings):
    # 对字符串进行处理 转换成列表
    new = []
    for i in strings:
        if (i == '#') and (len(new) != 0):
            new.pop()
        elif (i == '#') and (len(new) == 0):
            pass
        else:
            new.append(i)

    return new


def compare(s, t):
    # 比较字符串
    if s == t:
        return True
    else:
        return False

#s1 = string_process(s)
t1 = string_process(t)
compare(s1, t1)


