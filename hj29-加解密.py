# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 20:46:17 2022

@author: xuk11
"""

text1 = 'abcdefg'
text2 = 'BCDEFGH'

def encrypt_text(strs):
    # 加密字符串
    res = []
    for s in strs:
        if (ord(s) >= 97) and (ord(s) < 122):  # a-y
            res.append(chr(ord(s) + 1 - 32))
        elif s == 'z':
            res.append('A')
        elif (ord(s) >= 65) and (ord(s) < 90):  # A-Y
            res.append(chr(ord(s) + 1 + 32))
        elif s == 'Z':
            res.append('a')
        elif (ord(s) >= 48) and (ord(s) < 57):  # 0-8
            res.append(chr(ord(s) + 1))
        elif s == '9':
            res.append('0')
        else:
            res.append(s)

    return ''.join(res)


def decrypt_text(strs):
    # 解密
    res = []
    for s in strs:
        if (ord(s) > 97) and (ord(s) <= 122):  # b-z
            res.append(chr(ord(s) - 32 - 1))
        elif s == 'a':
            res.append('Z')
        elif (ord(s) > 65) and (ord(s) <= 90):  # B-Z
            res.append(chr(ord(s) + 32 - 1))
        elif s == 'A':
            res.append('z')
        elif (ord(s) > 48) and (ord(s) <= 57):  # 1-9
            res.append(chr(ord(s) - 1))
        elif s == '0':
            res.append('9')
        else:
            res.append(s)

    return ''.join(res)


print(encrypt_text(text1))
print(decrypt_text(text2))
