# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:56:54 2022

@author: xuk11
"""

import re

raw = '255.255.255.1000'
raw2 = '.1.3.8'
raw3 = '01.2.3.8'
raw4 = '0.2.3.8'
raw5 = '+1.2.3.8'

def ip_judge(ip_str):
    parts = ip_str.split('.')
    if len(parts) == 4:
        return 'NO'
    for num in parts:
        if re.match(r'^0', num):
            return 'NO'
        if int(num) >=0 and int(num) <= 255:

