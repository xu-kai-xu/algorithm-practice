# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:20:05 2022

@author: xuk11

学习别人的解法
https://www.nowcoder.com/practice/c466d480d20c4c7c9d322d12ca7955ac?tpId=196&tqId=37066&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D196&difficulty=undefined&judgeStatus=undefined&tags=&title=
"""

# s = 'aa'
# t = 'aaa'

s = "XDOYEZODEYXNZ"
t = "XYZ"

def check(hash):
    for key, value in hash.items():
        if value < 0:
            return False
    return True

def minWindow(S, T):
    cnt = len(S) + 1

    # 记录目标字符串T的字符个数
    hash = dict()
    for i in range(len(T)):
        if T[i] in hash:
            hash[T[i]] -= 1  # 处理重复字符的情况
        else:
            hash[T[i]] = -1

    slow = fast = 0
    left = right = -1  # 记录左右区间

    while fast < len(S):
        c = S[fast]
        if c in hash:
            hash[c] += 1  # 匹配，字符+1

        while check(hash):
            # 当hash表值全大于-1，说明全覆盖，此时缩小窗口
            # 取最优解
            if cnt > fast - slow + 1:
                cnt = fast - slow + 1
                left = slow
                right = fast
            c = S[slow]

            if c in hash:
                hash[c] -= 1  # 这一步还原字典

            slow += 1  # 缩小窗口
        fast += 1

    if left == -1:  # 左窗口没有更新过，说明没有找到
        return ''

    return S[left: right+1]



minWindow(s, t)







