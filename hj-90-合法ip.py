# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:39:50 2022

@author: xuk11
"""

import re

raw = '255.255.255.1000'
raw2 = '.1.3.8'
raw3 = '01.2.3.8'
raw4 = '0.2.3.8'
raw5 = '+1.2.3.8'


def ip_parse(raw_str):
    if re.search(r'[^0-9.]', raw_str):
        return 'NO'
    parts = raw_str.split('.')
    for num in parts:
        if re.match(r'^0\d', num):
            return 'NO'
    try:
        parts = [int(item) for item in raw_str.split('.')]
    except ValueError:
        return 'NO'
    return parts


def ip_judge(ip_lst):
    if len(ip_lst) != 4:
        return 'NO'

    for num in ip_lst:
        if (num < 0) or (num > 255):
            return('NO')
    return('YES')

ip = ip_parse(raw2)
ip_judge(ip)

