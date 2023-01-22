# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:35:53 2022

@author: xuk11
"""
I0 = '15 123 456 786 453 46 7 5 3 665 453456 745 456 786 453 123'
R0 = '5 6 3 6 3 0'

I = [tmp for tmp in I0.split(' ')[1:]]
R = [int(tmp) for tmp in R0.split(' ')[1:]]
R = map(str, (sorted(set(R))))

#R = map(str,sorted(map(int,set(R0.split()[1:]))))

totalNum = 0
res = ''

for num in R:
    singleRes, count = '', 0
    for i, v in enumerate(I):
        if num in v:
            singleRes += str(i) + ' ' + v + ' '
            totalNum += 2
            count += 1

    if count:
        singleRes = num + ' ' + str(count) + ' ' + singleRes
        totalNum += 2
    res += singleRes

print((str(totalNum) + ' ' + res).rstrip())

