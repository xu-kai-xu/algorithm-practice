# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:45:33 2022

@author: xuk11
"""
import re

def regex(opes_lst):
    """input: list"""
    res = []
    ptn = r"^([WSAD]{1})(\d{1,2})$"
    for i in opes_lst:
        tmp = re.match(ptn, i)
        if tmp:
            res.append((tmp.group(1), int(tmp.group(2))))
    return res

def move(leg_opes):
    """input: list"""
    x, y = 0, 0
    for (direc, dist) in leg_opes:
        if direc == 'A':
            x -= dist
        elif direc == 'D':
            x += dist
        elif direc == 'W':
            y += dist
        elif direc == 'S':
            y -= dist
    return (x, y)


a = 'A10;S20;W10;D30;X;A1A;B10A11;;A10;'
opes = a.split(";")

leg_opes = regex(opes)

res = move(leg_opes)



