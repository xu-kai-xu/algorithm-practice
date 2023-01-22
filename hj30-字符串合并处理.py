# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:00:01 2022

@author: xuk11

hj30 字符串合并处理
https://www.nowcoder.com/practice/d3d8e23870584782b3dd48f26cb39c8f?tpId=37&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu
"""
import re

raw = ['dec', 'fab']
#raw = ['123', '15']

# step 1
step1 = raw[0] + raw[1]

# step 2
even = []
odd = []
step2 = ''

for i in range(0, len(step1), 2):
    try:
        even.append(step1[i])
        odd.append(step1[i + 1])
    except IndexError:
        pass

# 排序
even.sort()
odd.sort()

i = 0
while True:
    try:
        step2 += even[i]
        step2 += odd[i]
        i += 1
    except IndexError:
        break

# step 3
step3 = ''
def crazy_trans(strs):
    """讨厌的转换，输入为字符"""
    if re.match(r'[0-9A-Fa-f]', strs):
        tmp = bin(int(strs, 16))[2:].zfill(4)[::-1] # 转换二进制并翻转
        tmp = hex(int(tmp, 2))
        return tmp[2:].upper()
    return strs

for s in step2:
    step3 += crazy_trans(s)

print(step3)
