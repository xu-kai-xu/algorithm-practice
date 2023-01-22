# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:36:08 2022

@author: xuk11

hj21 简单密码
https://www.nowcoder.com/practice/7960b5038a2142a18e27e4c733855dac?tpId=37&tqId=21243&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

转换规则：
1  1
abc 2
def 3
ghi 4
jkl 5
mno 6
pqrs 7
tuv 8
wxyz 9
0 0

大写，变成小写之后往后移一位

"""

raw = ['YUANzhi1987']
test = raw[0]

def encoding(char):
    """
    char encoding
    input: char
    """
    if char == '0':
        return char
    elif char == '1':
        return char
    elif (ord(char) >= 97) and (ord(char) < 100):
        return '2'  # abc
    elif (ord(char) >= 100) and (ord(char) < 103):
        return '3'  # def
    elif (ord(char) >= 103) and (ord(char) < 106):
        return '4'  # ghi
    elif (ord(char) >= 106) and (ord(char) < 109):
        return '5'  # jkl
    elif (ord(char) >= 109) and (ord(char) < 112):
        return '6'  # mno
    elif (ord(char) >= 112) and (ord(char) < 116):
        return '7'  # pqrs
    elif (ord(char) >= 116) and (ord(char) < 119):
        return '8'  # tuv
    elif (ord(char) >= 119) and (ord(char) < 123):
        return '9'  # wxyz
    elif (ord(char) >= 65) and (ord(char) < 90):
        return chr(ord(char) + 33)
    elif char == 'Z':
        return 'a'
    else:
        return char



res = ''
for s in raw[0]:
    res += encoding(s)

