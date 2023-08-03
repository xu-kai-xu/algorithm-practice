# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:24:08 2022

@author: xuk11
"""

import re

raw1 = '151121.15'
raw2 =  '1010.00'
raw3 = '0.85'
raw = raw3

res = '人民币'

digits = {1: '壹', 2: '贰', 3: '叁',
         4: '肆', 5: '伍', 6: '陆',
         7: '柒', 8: '捌', 9: '玖', 0: '零'}

places = {'元': '', '万': '', '亿': ''}

integer, decimal = raw.split('.')


# 整数部分
size = len(integer)
rev = integer[::-1]  # 翻转之后从个位开始分割
parts = []
while len(rev) > 4:
    parts.append(rev[:4])
    rev = rev[4:]

parts.append(rev)

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

for i in range(len(parts)):
    parts[i] = parts[i][::-1]  # 列表中每个字符串翻转，回复本组顺序


assert(''.join(parts[::-1]) == str(integer))  # 判断分割是否正确


# 转换
for i in range(len(parts)):
    if i == 0:
        places['元'] += parse_num(parts[i])
    if i == 1:
        places['万'] += parse_num(parts[i])
    if i == 2:
        places['亿'] += parse_num(parts[i])

if len(places['亿']) > 0:
    res += places['亿'] + '亿' + places['万'] + '万' + places['元'] + '元'
elif len(places['万']) > 0:
    res += places['万'] + '万' + places['元'] + '元'
elif (len(places['元']) > 0) and (int(integer) > 0):
    res += places['元'] + '元'


# 小数部分
if decimal == '00':
    res += '整'
elif decimal[0] == '0' and decimal[1] != '0':
    res += digits[int(decimal[1])] + '分'
elif decimal[0] != '0' and decimal[1] == '0':
    res += digits[int(decimal[0])] + '角'
else:
    res += digits[int(decimal[0])] + '角' + digits[int(decimal[1])] + '分'


res = res.replace('拾零', '拾')
res = res.replace('壹拾', '拾')

while True:
    if re.search('零{2,}', res):
        re.sub('零{2,}', '零', res)
    else:
        break

print(res)


