# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:37:00 2022

@author: xuk11
"""
from math import sqrt



def is_prime(n):
    if n == 1:
        return False
    elif (n == 2) or (n == 3):
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True
