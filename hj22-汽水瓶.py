# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:07:48 2022

@author: xuk11
"""

n = [3, 10, 81, 0]

def cola(n):
    a = n // 3
    b = n - 3 * a
    if (a == 0) and (b == 2):
        return 1
    elif (a == 0) and (b == 1):
        return 0
    else:
        return a + cola(a+b)