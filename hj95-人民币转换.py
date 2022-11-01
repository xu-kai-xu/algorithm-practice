# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:24:08 2022

@author: xuk11
"""

raw1 = '151121.15'
raw2 =  '1010.00'
raw = raw1

res = '人民币'

digits = {1: '壹', 2: '贰', 3: '叁',
         4: '肆', 5: '伍', 6: '陆',
         7: '柒', 8: '捌', 9: '玖', 0: '零'}


places = {100000000: '亿',
          10000000: '仟万', 1000000: '佰万',
          100000: '拾万', 10000: '万',
          1000: '仟', 100: '佰', 10: '拾'}

integer, decimal = raw.split('.')


# 整数部分
size = len(integer)
for i in range(size):
    for key in places:
        num = int(integer[i:]) // key
        if (num > 0) and (num < 10):
            res += digits[num] + places[key]
            # print(num)
            break


# 小数部分
if decimal == '00':
    res += '整'
elif decimal[0] == '0' and decimal[1] != '0':
    res += digits[int(decimal[1])] + '分'
elif decimal[0] != '0' and decimal[1] == '0':
    res += digits[int(decimal[0])] + '角'
else:
    res += digits[int(decimal[0])] + '角' + digits[int(decimal[1])] + '分'




