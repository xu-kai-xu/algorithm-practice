# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 08:51:06 2022

@author: xuk11
"""

# s = "XDOYEZODEYXNZ"
# t = "XYZ"

# s = 'a'
# t = 'aa'

# s = 'aa'
# t = 'aa'

# s = 'ab'
# t = 'b'

s = 'aa'
t = 'aaa'

def check(hash_dict):
    for key, item in hash_dict.items():
        if item < 0:
            return False
    return True


def minWindow(S, T):

    # write code here
    count = {}  # 初始化计数字典
    for item in T:
        if item in count:
            count[item] += -1  # 处理重复字符的情况
        else:
            count[item] = -1

    fast = slow = 0
    left = right = -1
    size = len(S)
    cnt = size + 1

    while fast < size:
        c = S[fast]
        if c in T:
            count[c] += 1

        while check(count):
            if cnt > (fast - slow + 1):
                cnt = fast - slow + 1
                left = slow
                right = fast

            c = S[slow]
            if c in count:
                count[c] -= 1

            slow += 1
        fast += 1

    if left == -1:
        return ''
    return S[left: right+1]


minWindow(s, t)
