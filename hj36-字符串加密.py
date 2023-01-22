# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:33:23 2022

@author: xuk11
"""

key = 'nihao'
text = 'ni'


def encrypt_text(strs, keys):
    # 加密
    old = [chr(i) for i in range(97, 123)]

    new = []
    for s in key:
        if s not in new:
            new.append(s)

    for m in old:
        if m not in new:
            new.append(m)

    encry_dict = {}
    for i in range(26):
        encry_dict[old[i]] = new[i]

    res = ''
    for n in strs:
        res += encry_dict[n]

    return res


print(encrypt_text(text, key))

