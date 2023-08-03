# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:39:53 2022

@author: xuk11

hj33 ip 地址与整数转换
https://www.nowcoder.com/practice/66ca0e28f90c42a196afd78cc9c496ea?tpId=37&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu
"""

raw = ['10.0.3.193', '167969729']

def ip_to_int(strs):
    """输入字符串"""
    ip = strs.split('.')
    segs = [bin(int(item))[2:].zfill(8) for item in ip]
    res = '0b'
    for i in segs:
        res += i

    res = int(res, 2)
    return res

def int_to_ip(strs):
    bins = bin(int(strs))[2:].zfill(32)
    segs = []
    for i in range(0, len(bins), 8):
        segs.append(str(int('0b' + bins[i: i+8], 2)))

    res = '.'.join(segs)
    return res


for item in raw:
    if '.' in item:
        print(ip_to_int(item))
    else:
        print(int_to_ip(item))
