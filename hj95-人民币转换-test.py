# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:40:02 2022

@author: xuk11
"""

parts = ['1010']

digits = {1: '壹', 2: '贰', 3: '叁',
         4: '肆', 5: '伍', 6: '陆',
         7: '柒', 8: '捌', 9: '玖', 0: '零'}

def parse_num(strs):
    units = {1000: '仟', 100: '佰', 10: '拾', 1: ''}
    resu = ''
    size = len(strs)
    for i in range(size):
        if int(strs[i]) == 0:
            resu += digits[int(strs[i])]
            continue
        for unit in units:
            if (int(strs[i:]) // unit) > 0 and (int(strs[i:]) // unit) < 10:
                resu += digits[int(strs[i])] + units[unit]

    return resu


parse_num(parts[0])

t = '壹仟零壹拾零'
t.replace('拾零', '拾')