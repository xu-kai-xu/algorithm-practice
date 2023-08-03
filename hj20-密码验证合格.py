# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:05:17 2022

@author: xuk11

hj20 密码验证

1. 长度超过8位，
2. 大写字母 小写字母 数字 其他字符

3. 不能有长度大于2的包含公共元素的子串重复
4. 其他符号不包括空格和换行。

匹配重复子串：https://www.jianshu.com/p/f5e64223a3ef


"""
import re

raw = ['021Abc9000',
        '021Abc9Abc1',
        '021ABC9000',
        '021$bc9000']

for item in raw:
    print(item)


def pass_eval(strs):
    """Password evaluation."""
    a, b, c, d = 0, 0, 0, 0
    size = len(strs)
    if size < 8:  # 长度超过 8 位
        return 'NG'
    if re.search(r'[a-z]', strs):
        a = 1
    if re.search(r'[A-Z]', strs):
        b = 1
    if re.search(r'[0-9]', strs):
        c = 1
    if re.search(r'[^a-zA-Z0-9\s]', strs):
        d = 1
    if sum([a, b, c, d]) < 3:
        return 'NG'
    if re.search(r'(.{3,}).*\1', strs):
        return 'NG'

    return 'OK'



